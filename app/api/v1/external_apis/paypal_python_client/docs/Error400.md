# Error400

Request is not well-formed, syntactically incorrect, or violates schema.

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
from openapi_client.models.error400 import Error400

# TODO update the JSON string below
json = "{}"
# create an instance of Error400 from a JSON string
error400_instance = Error400.from_json(json)
# print the JSON string representation of the object
print Error400.to_json()

# convert the object into a dict
error400_dict = error400_instance.to_dict()
# create an instance of Error400 from a dict
error400_form_dict = error400.from_dict(error400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


