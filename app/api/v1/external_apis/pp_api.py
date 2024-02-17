from base_api import BaseApi

import requests


class PayPalAPI(BaseApi):
    def __init__(self, client_id, client_secret):
        super().__init__("https://api-m.paypal.com")
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {
        }

    def get_oauth_token(self):
        auth_data = {"grant_type": "client_credentials"}
        auth_response = requests.post(self.base_url + "/v1/oauth2/token", auth=(self.client_id, self.client_secret), data=auth_data, headers=self.headers)
        json = auth_response.json()
        print(json)
        print()
        if auth_response.status_code == 200:
            self.headers['Authorization'] = "Bearer " + json['access_token']
        else:
            auth_response.raise_for_status()

    def search_transactions(self, start_date: str, end_date: str, transaction_type: str = None):
        #do this every time
        self.get_oauth_token()
        params = {"start_date": start_date, "end_date": end_date}
        if transaction_type:
            params['transaction_type'] = transaction_type
        #mak sure to only put in non base part of the url when call make_request
        return self.make_request("/v1/reporting/transactions", "GET", headers=self.headers, params=params)
        
# Example call
paypal_api = PayPalAPI('AcDpeX9nbG4qRF3NXXhq4PcrtlP7-0fbF7XBSaMxpboQpQStViOMKMlqVGfJ0wrSDWg71_Zp1w06hFY_', 'EITIFRLCoS05rQd5cqDRkPkjjduQZ4AHOWkPFHwSjN-D8L2CgsQ6nCcbzsrEt40BvVTBFZSzcRGtGB8P')
transactions = paypal_api.search_transactions('2023-07-01T00:00:00-0700', '2023-07-03T00:00:00-0700')
print(transactions['transaction-details'])