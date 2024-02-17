# Error415

The server does not support the request payload's media type.

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
from openapi_client.models.error415 import Error415

# TODO update the JSON string below
json = "{}"
# create an instance of Error415 from a JSON string
error415_instance = Error415.from_json(json)
# print the JSON string representation of the object
print Error415.to_json()

# convert the object into a dict
error415_dict = error415_instance.to_dict()
# create an instance of Error415 from a dict
error415_form_dict = error415.from_dict(error415_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


