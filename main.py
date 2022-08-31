# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests

from flight_search import FlightSearch
from notification_manager import NotificationManager

APP_ID = "52d211e5"
API_KEY = "2fa11a1f03d05e1c113399c4f1022129"

SHEET_NAME = "prices"
PROJECT_NAME = "flightDeals"
USERNAME = "7e2b5fd75fcd8d9752071375c3b98cfb"

SHEET_API_URL = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

flight_search = FlightSearch()
notification_manager = NotificationManager()

flight_search.data_manager.upadate_sheet(flight_search.price, flight_search.departure, flight_search.arrival,
                                         flight_search.link, flight_search.nights)


response = requests.get(url=SHEET_API_URL, headers=headers)
data = response.json()

for index in range(len(flight_search.price)):
    city = data["prices"][index]["city"]
    try:
        if data["prices"][index]["lowestPrice [euro]"] > data["prices"][index]["currentLowest"]:
            notification_manager.send_msg(city, flight_search.price[index], flight_search.departure[index],
                                          flight_search.nights[index], flight_search.link[index])
    except TypeError:
        pass


