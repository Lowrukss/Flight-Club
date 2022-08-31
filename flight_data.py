import requests


APP_ID = "52d211e5"
API_KEY = "2fa11a1f03d05e1c113399c4f1022129"

SHEET_NAME = "Flight Deals"
PROJECT_NAME = "Flight Deals"
USERNAME = "1Xw4n16LiRuHQYzK1oZiNi4AbnTSMFN6DBH-woEjE70E"

SHEET_API_URL = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.response = requests.get(url=SHEET_API_URL, headers=HEADERS)
        self.data = self.response.json()
