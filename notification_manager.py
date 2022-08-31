from twilio.rest import Client

ACCOUNT_SID = 'ACd037b7f78052ce6ce496025f2eac5828'
AUTH_TOKEN = '468ef11bb662d8cbf3ccc260345b409e'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_msg(self, flight_dest, flight_price, flight_departure, days_in_dest, link_to_offer):
        message = self.client.messages.create(
            body=f"Only €{flight_price} to fly from Warsaw to {flight_dest}, "
                 f"at {flight_departure} for {days_in_dest} days, link to offer: {link_to_offer}",
            from_="+13605640645",
            to="+48604557931"
        )
        print(message.sid)
