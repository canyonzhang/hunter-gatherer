# StoreInfo

The store information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | The ID of a store for a merchant in the system of record. | [optional] 
**terminal_id** | **str** | The terminal ID for the checkout stand in a merchant store. | [optional] 

## Example

```python
from openapi_client.models.store_info import StoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StoreInfo from a JSON string
store_info_instance = StoreInfo.from_json(json)
# print the JSON string representation of the object
print StoreInfo.to_json()

# convert the object into a dict
store_info_dict = store_info_instance.to_dict()
# create an instance of StoreInfo from a dict
store_info_form_dict = store_info.from_dict(store_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


