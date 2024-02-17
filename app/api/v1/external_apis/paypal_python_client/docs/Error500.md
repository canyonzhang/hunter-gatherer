# Error500

This is either a system or application error, and generally indicates that although the client appeared to provide a correct request, something unexpected has gone wrong on the server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**debug_id** | **str** | The PayPal internal ID. Used for correlation purposes. | [optional] 
**links** | [**List[ErrorLinkDescription]**](ErrorLinkDescription.md) | An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS). | [optional] 

## Example

```python
from openapi_client.models.error500 import Error500

# TODO update the JSON string below
json = "{}"
# create an instance of Error500 from a JSON string
error500_instance = Error500.from_json(json)
# print the JSON string representation of the object
print Error500.to_json()

# convert the object into a dict
error500_dict = error500_instance.to_dict()
# create an instance of Error500 from a dict
error500_form_dict = error500.from_dict(error500_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


