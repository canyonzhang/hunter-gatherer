# Error401

Authentication failed due to missing Authorization header, or invalid authentication credentials.

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
from openapi_client.models.error401 import Error401

# TODO update the JSON string below
json = "{}"
# create an instance of Error401 from a JSON string
error401_instance = Error401.from_json(json)
# print the JSON string representation of the object
print Error401.to_json()

# convert the object into a dict
error401_dict = error401_instance.to_dict()
# create an instance of Error401 from a dict
error401_form_dict = error401.from_dict(error401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


