# openapi-client
Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.9
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    except ApiException as e:
        print("Exception when calling BalancesApi->balances_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-m.paypal.com/v1/reporting*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BalancesApi* | [**balances_get**](docs/BalancesApi.md#balances_get) | **GET** /v1/reporting/balances | List all balances
*TransactionsApi* | [**search_get**](docs/TransactionsApi.md#search_get) | **GET** /v1/reporting/transactions | List transactions


## Documentation For Models

 - [Address](docs/Address.md)
 - [AuctionInfo](docs/AuctionInfo.md)
 - [BalanceDetail](docs/BalanceDetail.md)
 - [BalancesResponse](docs/BalancesResponse.md)
 - [CartInfo](docs/CartInfo.md)
 - [CheckoutOption](docs/CheckoutOption.md)
 - [Error400](docs/Error400.md)
 - [Error401](docs/Error401.md)
 - [Error403](docs/Error403.md)
 - [Error404](docs/Error404.md)
 - [Error409](docs/Error409.md)
 - [Error415](docs/Error415.md)
 - [Error422](docs/Error422.md)
 - [Error500](docs/Error500.md)
 - [Error503](docs/Error503.md)
 - [ErrorDefault](docs/ErrorDefault.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ErrorLinkDescription](docs/ErrorLinkDescription.md)
 - [ErrorLocation](docs/ErrorLocation.md)
 - [IncentiveDetail](docs/IncentiveDetail.md)
 - [IncentiveInfo](docs/IncentiveInfo.md)
 - [ItemDetail](docs/ItemDetail.md)
 - [ItemDetailTaxAmount](docs/ItemDetailTaxAmount.md)
 - [LinkDescription](docs/LinkDescription.md)
 - [Money](docs/Money.md)
 - [Name](docs/Name.md)
 - [PayerInfo](docs/PayerInfo.md)
 - [Phone](docs/Phone.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [ShippingInfo](docs/ShippingInfo.md)
 - [StoreInfo](docs/StoreInfo.md)
 - [TransactionDetail](docs/TransactionDetail.md)
 - [TransactionInfo](docs/TransactionInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Oauth2"></a>
### Oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **https://uri.paypal.com/services/reporting/search/read**: Transactions Search
 - **https://uri.paypal.com/services/reporting/balances/read**: List Balances


## Author



