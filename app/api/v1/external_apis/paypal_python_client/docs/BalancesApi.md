# openapi_client.BalancesApi

All URIs are relative to *https://api-m.paypal.com/v1/reporting*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balances_get**](BalancesApi.md#balances_get) | **GET** /v1/reporting/balances | List all balances


# **balances_get**
> BalancesResponse balances_get(as_of_time=as_of_time, currency_code=currency_code)

List all balances

List all balances. Specify date time to list balances for that time that appear in the response.<blockquote><strong>Notes:</strong> <ul><li>It takes a maximum of three hours for balances to appear in the list balances call.</li><li>This call lists balances upto the previous three years.</li></ul></blockquote>

### Example

* OAuth Authentication (Oauth2):

```python
import openapi_client
from openapi_client.models.balances_response import BalancesResponse
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
    api_instance = openapi_client.BalancesApi(api_client)
    as_of_time = 'as_of_time_example' # str | List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided. (optional)
    currency_code = 'currency_code_example' # str | Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency. (optional)

    try:
        # List all balances
        api_response = api_instance.balances_get(as_of_time=as_of_time, currency_code=currency_code)
        print("The response of BalancesApi->balances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancesApi->balances_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_of_time** | **str**| List balances in the response at the date time provided, will return the last refreshed balance in the system when not provided. | [optional] 
 **currency_code** | **str**| Filters the transactions in the response by a [three-character ISO-4217 currency code](/api/rest/reference/currency-codes/) for the PayPal transaction currency. | [optional] 

### Return type

[**BalancesResponse**](BalancesResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful request returns the HTTP &#x60;200 OK&#x60; status code and a JSON response body that lists balances . |  -  |
**400** | The request is not well-formed, is syntactically incorrect, or violates schema. |  -  |
**403** | Authorization failed due to insufficient permissions. |  -  |
**500** | An internal server error occurred. |  -  |
**0** | The default response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

