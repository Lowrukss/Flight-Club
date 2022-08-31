import requests
import datetime as dt

APP_ID = "52d211e5"
API_KEY = "2fa11a1f03d05e1c113399c4f1022129"

SHEET_NAME = "prices"
PROJECT_NAME = "flightDeals"
USERNAME = "7e2b5fd75fcd8d9752071375c3b98cfb"

SHEET_API_URL = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=SHEET_API_URL, headers=HEADERS)
        self.data = self.response.json()

        self.iatacode = [row["iataCode"] for row in self.data["prices"]]

    def upadate_sheet(self, flight_price, flight_departure, flight_arrival, flight_link, nights_in_dest):
        for index in range(1, len(self.iatacode) + 1):
            sheet_inputs = {
                "price": {
                    "currentLowest": flight_price[index - 1],
                    "dateOfDeparture": flight_departure[index - 1],
                    "dateOfArrival": flight_arrival[index - 1],
                    "nightsInDestination": nights_in_dest[index - 1],
                    "linkToOffer": flight_link[index - 1],
                    "dayOfUpdate": dt.datetime.now().strftime("%d/%m/%Y")
                }
            }

            put = requests.put(url=f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}/{index + 1}",
                               json=sheet_inputs, headers=HEADERS)
            put.raise_for_status()
