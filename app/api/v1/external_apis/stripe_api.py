from base_api import BaseApi

import requests
import stripe

stripe.api_key = "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"


class StripeAPI(BaseApi):
    def __init__(self):
        super().__init__("https://api.stripe.com")
        self.headers = {
        }

    def search_transactions(self, start_date, end_date):
        try:
            # List charges for a specific customer and optionally within a certain time range
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,  # timestamp for one week ago
                    "lt": end_date  # timestamp for now (feb 17th 2023 2:10:00)
                }
            )

            # Iterate through the charges and do something with them
            for charge in charges.auto_paging_iter():
                print(charge)
        except stripe.error.StripeError as e:
            # Handle error
            print(e)

    def get_donations(self, start_date, end_date):
        try:
            total_donations = []
            charges = stripe.Charge.list(
                created={
                    "gte": start_date,
                    "lt": end_date
                }
            )

            for charge in charges.auto_paging_iter():
                if 'Donation' in charge.get('description'):
                    total_donations.append(charge)

            return total_donations
        except stripe.error.StripeError as e:
            print(e)
            return None


stripe_api = StripeAPI()
stripe_api.search_transactions(1707602577, 1708207377)

donations = stripe_api.get_donations(1672614308, 1704063908)

if donations:
    for donation in donations:
        print(f"Donation Transaction ID: {donation['id']}")
        print(f"Amount: {donation['amount'] / 100} {donation['currency']}")
        print(f"Description: {donation['description']}")
        print("-------------")
else:
    print("No donations found.")
