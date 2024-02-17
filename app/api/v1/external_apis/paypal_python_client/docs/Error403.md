# Error403

The client is not authorized to access this resource, although it may have valid credentials. 

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
from openapi_client.models.error403 import Error403

# TODO update the JSON string below
json = "{}"
# create an instance of Error403 from a JSON string
error403_instance = Error403.from_json(json)
# print the JSON string representation of the object
print Error403.to_json()

# convert the object into a dict
error403_dict = error403_instance.to_dict()
# create an instance of Error403 from a dict
error403_form_dict = error403.from_dict(error403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


