# Error404

The server has not found anything matching the request URI. This either means that the URI is incorrect or the resource is not available.

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
from openapi_client.models.error404 import Error404

# TODO update the JSON string below
json = "{}"
# create an instance of Error404 from a JSON string
error404_instance = Error404.from_json(json)
# print the JSON string representation of the object
print Error404.to_json()

# convert the object into a dict
error404_dict = error404_instance.to_dict()
# create an instance of Error404 from a dict
error404_form_dict = error404.from_dict(error404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


