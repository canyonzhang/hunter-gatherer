# ErrorDefault

The default error response.

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
from openapi_client.models.error_default import ErrorDefault

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDefault from a JSON string
error_default_instance = ErrorDefault.from_json(json)
# print the JSON string representation of the object
print ErrorDefault.to_json()

# convert the object into a dict
error_default_dict = error_default_instance.to_dict()
# create an instance of ErrorDefault from a dict
error_default_form_dict = error_default.from_dict(error_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


