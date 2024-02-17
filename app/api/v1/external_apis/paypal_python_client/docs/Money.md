# Money

The currency and amount for a financial transaction, such as a balance or payment due.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency. | 
**value** | **str** | The value, which might be:&lt;ul&gt;&lt;li&gt;An integer for currencies like &#x60;JPY&#x60; that are not typically fractional.&lt;/li&gt;&lt;li&gt;A decimal fraction for currencies like &#x60;TND&#x60; that are subdivided into thousandths.&lt;/li&gt;&lt;/ul&gt;For the required number of decimal places for a currency code, see [Currency Codes](/docs/integration/direct/rest/currency-codes/). | 

## Example

```python
from openapi_client.models.money import Money

# TODO update the JSON string below
json = "{}"
# create an instance of Money from a JSON string
money_instance = Money.from_json(json)
# print the JSON string representation of the object
print Money.to_json()

# convert the object into a dict
money_dict = money_instance.to_dict()
# create an instance of Money from a dict
money_form_dict = money.from_dict(money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


