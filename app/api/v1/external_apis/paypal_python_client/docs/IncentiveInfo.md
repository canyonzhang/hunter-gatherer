# IncentiveInfo

The incentive details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incentive_details** | [**List[IncentiveDetail]**](IncentiveDetail.md) | An array of incentive details. | [optional] 

## Example

```python
from openapi_client.models.incentive_info import IncentiveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IncentiveInfo from a JSON string
incentive_info_instance = IncentiveInfo.from_json(json)
# print the JSON string representation of the object
print IncentiveInfo.to_json()

# convert the object into a dict
incentive_info_dict = incentive_info_instance.to_dict()
# create an instance of IncentiveInfo from a dict
incentive_info_form_dict = incentive_info.from_dict(incentive_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


