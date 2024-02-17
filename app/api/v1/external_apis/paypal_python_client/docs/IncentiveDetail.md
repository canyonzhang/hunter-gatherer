# IncentiveDetail

The incentive details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incentive_type** | **str** | The type of incentive, such as a special offer or coupon. | [optional] 
**incentive_code** | **str** | The code that identifies an incentive, such as a coupon. | [optional] 
**incentive_amount** | [**Money**](Money.md) |  | [optional] 
**incentive_program_code** | **str** | The incentive program code that identifies a merchant loyalty or incentive program. | [optional] 

## Example

```python
from openapi_client.models.incentive_detail import IncentiveDetail

# TODO update the JSON string below
json = "{}"
# create an instance of IncentiveDetail from a JSON string
incentive_detail_instance = IncentiveDetail.from_json(json)
# print the JSON string representation of the object
print IncentiveDetail.to_json()

# convert the object into a dict
incentive_detail_dict = incentive_detail_instance.to_dict()
# create an instance of IncentiveDetail from a dict
incentive_detail_form_dict = incentive_detail.from_dict(incentive_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


