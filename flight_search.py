import requests
import datetime as dt
from data_manager import DataManager

FLIGHT_DEALS_API_KEY = "00jpoljX77rCEdFiNwFD1IV36lME_5Tu"
TEQUILA_DEFAULT_API = "https://tequila-api.kiwi.com/v2/search?"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data_manager = DataManager()

        self.price = []
        self.departure = []
        self.arrival = []
        self.nights = []
        self.link = []

        self.timedelta = dt.timedelta(days=60)
        self.datefrom = dt.datetime.now().strftime("%d/%m/%Y")
        self.dateto = (dt.datetime.now() + self.timedelta).strftime("%d/%m/%Y")

        self.header = {
            "apikey": FLIGHT_DEALS_API_KEY
        }

        for iata in self.data_manager.iatacode:
            self.tequila_parameters = {
                "fly_from": "WAW",
                "fly_to": iata,
                "dateFrom": self.datefrom,
                "dateTo": self.dateto,
                "nights_in_dst_from": 3,
                "nights_in_dst_to": 8,
                "max_stopovers": 0
            }

            self.response = requests.get(url=TEQUILA_DEFAULT_API, params=self.tequila_parameters, headers=self.header)
            self.flight_data = self.response.json()

            self.price.append(self.get_price())
            self.departure.append(self.get_departure_date())
            self.arrival.append(self.get_arrival_date())
            self.nights.append(self.get_nights_in_dest())
            self.link.append(self.get_link_to_offer())

    def get_price(self):
        try:
            return self.flight_data["data"][0]["price"]
        except IndexError:
            return "NO FLIGHT AVAILABLE"

    def get_departure_date(self):
        try:
            return self.flight_data["data"][0]["local_departure"]
        except IndexError:
            return "NO FLIGHT AVAILABLE"

    def get_arrival_date(self):
        try:
            return self.flight_data["data"][0]["local_arrival"]
        except IndexError:
            return "NO FLIGHT AVAILABLE"

    def get_link_to_offer(self):
        try:
            return self.flight_data["data"][0]["deep_link"]
        except IndexError:
            return "NO FLIGHT AVAILABLE"

    def get_nights_in_dest(self):
        try:
            return self.flight_data["data"][0]["nightsInDest"]
        except IndexError:
            return "NO FLIGHT AVAILABLE"
