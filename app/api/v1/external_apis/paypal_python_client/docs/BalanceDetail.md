# BalanceDetail

The Balance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The [three-character ISO-4217 currency code](/docs/integration/direct/rest/currency-codes/) that identifies the currency. | 
**primary** | **bool** | Optional field representing if the currency is primary currency or not. | [optional] 
**total_balance** | [**Money**](Money.md) |  | 
**available_balance** | [**Money**](Money.md) |  | [optional] 
**withheld_balance** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.balance_detail import BalanceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceDetail from a JSON string
balance_detail_instance = BalanceDetail.from_json(json)
# print the JSON string representation of the object
print BalanceDetail.to_json()

# convert the object into a dict
balance_detail_dict = balance_detail_instance.to_dict()
# create an instance of BalanceDetail from a dict
balance_detail_form_dict = balance_detail.from_dict(balance_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


