# Error503

The server is temporarily unable to handle the request, for example, because of planned maintenance or downtime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**debug_id** | **str** | The PayPal internal ID. Used for correlation purposes. | [optional] 
**links** | [**List[ErrorLinkDescription]**](ErrorLinkDescription.md) | An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS). | [optional] 

## Example

```python
from openapi_client.models.error503 import Error503

# TODO update the JSON string below
json = "{}"
# create an instance of Error503 from a JSON string
error503_instance = Error503.from_json(json)
# print the JSON string representation of the object
print Error503.to_json()

# convert the object into a dict
error503_dict = error503_instance.to_dict()
# create an instance of Error503 from a dict
error503_form_dict = error503.from_dict(error503_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


