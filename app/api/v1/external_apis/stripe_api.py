from base_api import BaseApi
from dotenv import load_dotenv
from pathlib import Path
import os                                                                                                                                                                                                          


import requests
import stripe
from datetime import datetime

load_dotenv()
stripe.api_key = os.getenv("Stripe_SECRET_KEY")


class StripeAPI(BaseApi):
    def __init__(self):
        super().__init__("https://api.stripe.com")
        self.headers = {
        }
    
    def search_transactions(self, start_date, end_date):
        try:
            # List charges for a specific customer and optionally within a certain time range
            # donations = stripe.
            # print(len(donations))
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,  # greater than or equal to timestamp for one week ago
                    "lt": end_date    # less than timestamp til now (~feb 17th 2023 2:10:00)
                }
            )
            
            # Iterate through the charges and do something with them
            for charge in charges.auto_paging_iter():
                print(f"Name: {charge['billing_details']['name']}, "
                    f"Amount: {charge['amount']}, "
                    f"Currency: {charge['currency']}, "
                    f"Date: {datetime.utcfromtimestamp(charge['created']).strftime('%Y-%m-%d %H:%M:%S')}, "
                    f"Application Fee: {charge.get('application_fee', 'N/A')}")
        except stripe.error.StripeError as e:
            # Handle error
            print(e)


stripe_api = StripeAPI()
stripe_api.search_transactions(1707602577, 1708207377)