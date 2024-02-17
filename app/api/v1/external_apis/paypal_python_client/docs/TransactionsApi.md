# openapi_client.TransactionsApi

All URIs are relative to *https://api-m.paypal.com/v1/reporting*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](TransactionsApi.md#search_get) | **GET** /v1/reporting/transactions | List transactions


# **search_get**
> SearchResponse search_get(start_date, end_date, transaction_id=transaction_id, transaction_type=transaction_type, transaction_status=transaction_status, transaction_amount=transaction_amount, transaction_currency=transaction_currency, payment_instrument_type=payment_instrument_type, store_id=store_id, terminal_id=terminal_id, fields=fields, balance_affecting_records_only=balance_affecting_records_only, page_size=page_size, page=page)

List transactions

Lists transactions. Specify one or more query parameters to filter the transaction that appear in the response.<blockquote><strong>Notes:</strong> <ul><li>If you specify one or more optional query parameters, the <code>ending_balance</code> response field is empty.</li><li>It takes a maximum of three hours for executed transactions to appear in the list transactions call.</li><li>This call lists transaction for the previous three years.</li></ul></blockquote>

### Example

* OAuth Authentication (Oauth2):

```python
import openapi_client
from openapi_client.models.search_response import SearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-m.paypal.com/v1/reporting
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api-m.paypal.com/v1/reporting"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TransactionsApi(api_client)
    start_date = 'start_date_example' # str | Filters the transactions in the response by a start date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required. Fractional seconds are optional.
    end_date = 'end_date_example' # str | Filters the transactions in the response by an end date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required. Fractional seconds are optional. The maximum supported range is 31 days.
    transaction_id = 'transaction_id_example' # str | Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID is 17 characters long, except for an <a href=\"/docs/api/payments/v1/#definition-order\">order ID</a>, which is 19 characters long.<blockquote><strong>Note:</strong> A transaction ID is not unique in the reporting system. The response can list two transactions with the same ID. One transaction can be balance affecting while the other is non-balance affecting.</blockquote> (optional)
    transaction_type = 'transaction_type_example' # str | Filters the transactions in the response by a PayPal transaction event code. See [Transaction event codes](/docs/integration/direct/transaction-search/transaction-event-codes/). (optional)
    transaction_status = 'transaction_status_example' # str | Filters the transactions in the response by a PayPal transaction status code. Value is:<table><thead><tr><th>Status&nbsp;code</th><th>Description</th></tr></thead><tbody><tr><td><code>D</code></td><td>PayPal or merchant rules denied the transaction.</td></tr><tr><td><code>P</code></td><td>The transaction is pending. The transaction was created but waits for another payment process to complete, such as an ACH transaction, before the status changes to <code>S</code>.</td></tr><tr><td><code>S</code></td><td>The transaction successfully completed without a denial and after any pending statuses.</td></tr><tr><td><code>V</code></td><td>A successful transaction was reversed and funds were refunded to the original sender.</td></tr></tbody></table> (optional)
    transaction_amount = 'transaction_amount_example' # str | Filters the transactions in the response by a gross transaction amount range. Specify the range as `<start-range> TO <end-range>`, where `<start-range>` is the lower limit of the gross PayPal transaction amount and `<end-range>` is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For example, to search for transactions from $5.00 to $10.05, specify `[500 TO 1005]`.<blockquote><strong>Note:</strong>The values must be URL encoded.</blockquote> (optional)
    transaction_currency = 'transaction_currency_example' # str | Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency. (optional)
    payment_instrument_type = 'payment_instrument_type_example' # str | Filters the transactions in the response by a payment instrument type. Value is either:<ul><li><code>CREDITCARD</code>. Returns a direct credit card transaction with a corresponding value.</li><li><code>DEBITCARD</code>. Returns a debit card transaction with a corresponding value.</li></ul>If you omit this parameter, the API does not apply this filter. (optional)
    store_id = 'store_id_example' # str | Filters the transactions in the response by a store ID. (optional)
    terminal_id = 'terminal_id_example' # str | Filters the transactions in the response by a terminal ID. (optional)
    fields = 'transaction_info' # str | Indicates which fields appear in the response. Value is a single field or a comma-separated list of fields. The <code>transaction_info</code> value returns only the transaction details in the response. To include all fields in the response, specify <code>fields=all</code>. Valid fields are:<ul><li><a href=\"/docs/api/transaction-search/v1/#definition-transaction_info\"><code>transaction_info</code></a>. The transaction information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID, the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and time when the transaction was initiated and was last updated, the transaction amounts including the PayPal fee, any discounts, insurance, the transaction status, and other information about the transaction.</li><li><a href=\"/docs/api/transaction-search/v1/#definition-payer_info\"><code>payer_info</code></a>. The payer information. Includes the PayPal customer account ID and the payer's email address, primary phone number, name, country code, address, and whether the payer is verified or unverified.</li><li><a href=\"/docs/api/transaction-search/v1/#definition-shipping_info\"><code>shipping_info</code></a>. The shipping information. Includes the recipient's name, the shipping method for this order, the shipping address for this order, and the secondary address associated with this order.</li><li><a href=\"/docs/api/transaction-search/v1/#definition-auction_info\"><code>auction_info</code></a>. The auction information. Includes the name of the auction site, the auction site URL, the ID of the customer who makes the purchase in the auction, and the date and time when the auction closes.</li><li><a href=\"/docs/api/transaction-search/v1/#definition-cart_info\"><code>cart_info</code></a>. The cart information. Includes an array of item details, whether the item amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated invoices.</li><li><a href=\"/docs/api/transaction-search/v1/#definition-incentive_info\"><code>incentive_info</code></a>. An array of incentive detail objects. Each object includes the incentive, such as a special offer or coupon, the incentive amount, and the incentive program code that identifies a merchant loyalty or incentive program.</li><li><a href=\"/docs/api/transaction-search/v1/#definition-store_info\"><code>store_info</code></a>. The store information. Includes the ID of the merchant store and the terminal ID for the checkout stand in the merchant store.</li></ul> (optional) (default to 'transaction_info')
    balance_affecting_records_only = 'Y' # str | Indicates whether the response includes only balance-impacting transactions or all transactions. Value is either:<ul><li><code>Y</code>. The default. The response includes only balance transactions.</li><li><code>N</code>. The response includes all transactions.</li></ul> (optional) (default to 'Y')
    page_size = 100 # int | The number of items to return in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items. The combination of `page=2` and `page_size=20` returns the next 20 items. (optional) (default to 100)
    page = 1 # int | The zero-relative start index of the entire list of items that are returned in the response. So, the combination of `page=1` and `page_size=20` returns the first 20 items. (optional) (default to 1)

    try:
        # List transactions
        api_response = api_instance.search_get(start_date, end_date, transaction_id=transaction_id, transaction_type=transaction_type, transaction_status=transaction_status, transaction_amount=transaction_amount, transaction_currency=transaction_currency, payment_instrument_type=payment_instrument_type, store_id=store_id, terminal_id=terminal_id, fields=fields, balance_affecting_records_only=balance_affecting_records_only, page_size=page_size, page=page)
        print("The response of TransactionsApi->search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Filters the transactions in the response by a start date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required. Fractional seconds are optional. | 
 **end_date** | **str**| Filters the transactions in the response by an end date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required. Fractional seconds are optional. The maximum supported range is 31 days. | 
 **transaction_id** | **str**| Filters the transactions in the response by a PayPal transaction ID. A valid transaction ID is 17 characters long, except for an &lt;a href&#x3D;\&quot;/docs/api/payments/v1/#definition-order\&quot;&gt;order ID&lt;/a&gt;, which is 19 characters long.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; A transaction ID is not unique in the reporting system. The response can list two transactions with the same ID. One transaction can be balance affecting while the other is non-balance affecting.&lt;/blockquote&gt; | [optional] 
 **transaction_type** | **str**| Filters the transactions in the response by a PayPal transaction event code. See [Transaction event codes](/docs/integration/direct/transaction-search/transaction-event-codes/). | [optional] 
 **transaction_status** | **str**| Filters the transactions in the response by a PayPal transaction status code. Value is:&lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Status&amp;nbsp;code&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;&lt;code&gt;D&lt;/code&gt;&lt;/td&gt;&lt;td&gt;PayPal or merchant rules denied the transaction.&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;code&gt;P&lt;/code&gt;&lt;/td&gt;&lt;td&gt;The transaction is pending. The transaction was created but waits for another payment process to complete, such as an ACH transaction, before the status changes to &lt;code&gt;S&lt;/code&gt;.&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;code&gt;S&lt;/code&gt;&lt;/td&gt;&lt;td&gt;The transaction successfully completed without a denial and after any pending statuses.&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;code&gt;V&lt;/code&gt;&lt;/td&gt;&lt;td&gt;A successful transaction was reversed and funds were refunded to the original sender.&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
 **transaction_amount** | **str**| Filters the transactions in the response by a gross transaction amount range. Specify the range as &#x60;&lt;start-range&gt; TO &lt;end-range&gt;&#x60;, where &#x60;&lt;start-range&gt;&#x60; is the lower limit of the gross PayPal transaction amount and &#x60;&lt;end-range&gt;&#x60; is the upper limit of the gross transaction amount. Specify the amounts in lower denominations. For example, to search for transactions from $5.00 to $10.05, specify &#x60;[500 TO 1005]&#x60;.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt;The values must be URL encoded.&lt;/blockquote&gt; | [optional] 
 **transaction_currency** | **str**| Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency. | [optional] 
 **payment_instrument_type** | **str**| Filters the transactions in the response by a payment instrument type. Value is either:&lt;ul&gt;&lt;li&gt;&lt;code&gt;CREDITCARD&lt;/code&gt;. Returns a direct credit card transaction with a corresponding value.&lt;/li&gt;&lt;li&gt;&lt;code&gt;DEBITCARD&lt;/code&gt;. Returns a debit card transaction with a corresponding value.&lt;/li&gt;&lt;/ul&gt;If you omit this parameter, the API does not apply this filter. | [optional] 
 **store_id** | **str**| Filters the transactions in the response by a store ID. | [optional] 
 **terminal_id** | **str**| Filters the transactions in the response by a terminal ID. | [optional] 
 **fields** | **str**| Indicates which fields appear in the response. Value is a single field or a comma-separated list of fields. The &lt;code&gt;transaction_info&lt;/code&gt; value returns only the transaction details in the response. To include all fields in the response, specify &lt;code&gt;fields&#x3D;all&lt;/code&gt;. Valid fields are:&lt;ul&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-transaction_info\&quot;&gt;&lt;code&gt;transaction_info&lt;/code&gt;&lt;/a&gt;. The transaction information. Includes the ID of the PayPal account of the payee, the PayPal-generated transaction ID, the PayPal-generated base ID, the PayPal reference ID type, the transaction event code, the date and time when the transaction was initiated and was last updated, the transaction amounts including the PayPal fee, any discounts, insurance, the transaction status, and other information about the transaction.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-payer_info\&quot;&gt;&lt;code&gt;payer_info&lt;/code&gt;&lt;/a&gt;. The payer information. Includes the PayPal customer account ID and the payer&#39;s email address, primary phone number, name, country code, address, and whether the payer is verified or unverified.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-shipping_info\&quot;&gt;&lt;code&gt;shipping_info&lt;/code&gt;&lt;/a&gt;. The shipping information. Includes the recipient&#39;s name, the shipping method for this order, the shipping address for this order, and the secondary address associated with this order.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-auction_info\&quot;&gt;&lt;code&gt;auction_info&lt;/code&gt;&lt;/a&gt;. The auction information. Includes the name of the auction site, the auction site URL, the ID of the customer who makes the purchase in the auction, and the date and time when the auction closes.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-cart_info\&quot;&gt;&lt;code&gt;cart_info&lt;/code&gt;&lt;/a&gt;. The cart information. Includes an array of item details, whether the item amount or the shipping amount already includes tax, and the ID of the invoice for PayPal-generated invoices.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-incentive_info\&quot;&gt;&lt;code&gt;incentive_info&lt;/code&gt;&lt;/a&gt;. An array of incentive detail objects. Each object includes the incentive, such as a special offer or coupon, the incentive amount, and the incentive program code that identifies a merchant loyalty or incentive program.&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/docs/api/transaction-search/v1/#definition-store_info\&quot;&gt;&lt;code&gt;store_info&lt;/code&gt;&lt;/a&gt;. The store information. Includes the ID of the merchant store and the terminal ID for the checkout stand in the merchant store.&lt;/li&gt;&lt;/ul&gt; | [optional] [default to &#39;transaction_info&#39;]
 **balance_affecting_records_only** | **str**| Indicates whether the response includes only balance-impacting transactions or all transactions. Value is either:&lt;ul&gt;&lt;li&gt;&lt;code&gt;Y&lt;/code&gt;. The default. The response includes only balance transactions.&lt;/li&gt;&lt;li&gt;&lt;code&gt;N&lt;/code&gt;. The response includes all transactions.&lt;/li&gt;&lt;/ul&gt; | [optional] [default to &#39;Y&#39;]
 **page_size** | **int**| The number of items to return in the response. So, the combination of &#x60;page&#x3D;1&#x60; and &#x60;page_size&#x3D;20&#x60; returns the first 20 items. The combination of &#x60;page&#x3D;2&#x60; and &#x60;page_size&#x3D;20&#x60; returns the next 20 items. | [optional] [default to 100]
 **page** | **int**| The zero-relative start index of the entire list of items that are returned in the response. So, the combination of &#x60;page&#x3D;1&#x60; and &#x60;page_size&#x3D;20&#x60; returns the first 20 items. | [optional] [default to 1]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request returns the HTTP &#x60;200 OK&#x60; status code and a JSON response body that lists transactions . |  -  |
**0** | The default response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

