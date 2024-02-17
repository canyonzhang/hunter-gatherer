# ErrorDetails

The error details. Required for client-side `4XX` errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The field that caused the error. If this field is in the body, set this value to the field&#39;s JSON pointer value. Required for client-side errors. | [optional] 
**value** | **str** | The value of the field that caused the error. | [optional] 
**location** | [**ErrorLocation**](ErrorLocation.md) |  | [optional] 
**issue** | **str** | The unique, fine-grained application-level error code. | 
**description** | **str** | The human-readable description for an issue. The description can change over the lifetime of an API, so clients must not depend on this value. | [optional] 

## Example

```python
from openapi_client.models.error_details import ErrorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetails from a JSON string
error_details_instance = ErrorDetails.from_json(json)
# print the JSON string representation of the object
print ErrorDetails.to_json()

# convert the object into a dict
error_details_dict = error_details_instance.to_dict()
# create an instance of ErrorDetails from a dict
error_details_form_dict = error_details.from_dict(error_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


