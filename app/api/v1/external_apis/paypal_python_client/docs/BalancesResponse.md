# BalancesResponse

The balances response information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[BalanceDetail]**](BalanceDetail.md) | An array of balance detail objects. | [optional] 
**account_id** | **str** | The PayPal payer ID, which is a masked version of the PayPal account number intended for use with third parties. The account number is reversibly encrypted and a proprietary variant of Base32 is used to encode the result. | [optional] 
**as_of_time** | **str** | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The regular expression provides guidance but does not reject all invalid dates.&lt;/blockquote&gt; | [optional] 
**last_refresh_time** | **str** | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The regular expression provides guidance but does not reject all invalid dates.&lt;/blockquote&gt; | [optional] 

## Example

```python
from openapi_client.models.balances_response import BalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalancesResponse from a JSON string
balances_response_instance = BalancesResponse.from_json(json)
# print the JSON string representation of the object
print BalancesResponse.to_json()

# convert the object into a dict
balances_response_dict = balances_response_instance.to_dict()
# create an instance of BalancesResponse from a dict
balances_response_form_dict = balances_response.from_dict(balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


