# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cart_info import CartInfo

class TestCartInfo(unittest.TestCase):
    """CartInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CartInfo:
        """Test CartInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CartInfo`
        """
        model = CartInfo()
        if include_optional:
            return CartInfo(
                item_details = [
                    openapi_client.models.item_details.Item Details(
                        item_code = '5''UOq1hlK5jZXw'V6.YZb0', 
                        item_name = '5''UOq1hlK5jZXw'V6.YZb0', 
                        item_description = '5''UOq1hlK5jZXw'V6.YZb0', 
                        item_options = '5''UOq1hlK5jZXw'V6.YZb0', 
                        item_quantity = '5''UOq1hlK5jZXw'V6.YZb0', 
                        item_unit_price = openapi_client.models.money.Money(
                            currency_code = '012', 
                            value = '-.2888001528021798096225500850', ), 
                        item_amount = openapi_client.models.money.Money(
                            currency_code = '012', 
                            value = '-.2888001528021798096225500850', ), 
                        discount_amount = , 
                        adjustment_amount = , 
                        gift_wrap_amount = , 
                        tax_percentage = '-.2888001528021798096225500850', 
                        tax_amounts = [
                            openapi_client.models.tax_amount.Tax Amount(
                                tax_amount = , )
                            ], 
                        basic_shipping_amount = , 
                        extra_shipping_amount = , 
                        handling_amount = , 
                        insurance_amount = , 
                        total_item_amount = , 
                        invoice_number = '5''UOq1hlK5jZXw'V6.YZb0', 
                        checkout_options = [
                            openapi_client.models.checkout_option.Checkout Option(
                                checkout_option_name = '5''UOq1hlK5jZXw'V6.YZb0', 
                                checkout_option_value = '5''UOq1hlK5jZXw'V6.YZb0', )
                            ], )
                    ],
                tax_inclusive = True,
                paypal_invoice_id = '5''UOq1hlK5jZXw'V6.YZb0'
            )
        else:
            return CartInfo(
        )
        """

    def testCartInfo(self):
        """Test CartInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()