# Error409

The server has detected a conflict while processing this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**details** | [**List[ErrorDetails]**](ErrorDetails.md) |  | [optional] 
**debug_id** | **str** | The PayPal internal ID. Used for correlation purposes. | [optional] 
**links** | [**List[ErrorLinkDescription]**](ErrorLinkDescription.md) | An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS). | [optional] 

## Example

```python
from openapi_client.models.error409 import Error409

# TODO update the JSON string below
json = "{}"
# create an instance of Error409 from a JSON string
error409_instance = Error409.from_json(json)
# print the JSON string representation of the object
print Error409.to_json()

# convert the object into a dict
error409_dict = error409_instance.to_dict()
# create an instance of Error409 from a dict
error409_form_dict = error409.from_dict(error409_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


