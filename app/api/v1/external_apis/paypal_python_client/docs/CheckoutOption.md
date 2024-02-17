# CheckoutOption

A checkout option as a name-and-value pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_option_name** | **str** | The checkout option name, such as &#x60;color&#x60; or &#x60;texture&#x60;. | [optional] 
**checkout_option_value** | **str** | The checkout option value. For example, the checkout option &#x60;color&#x60; might be &#x60;blue&#x60; or &#x60;red&#x60; while the checkout option &#x60;texture&#x60; might be &#x60;smooth&#x60; or &#x60;rippled&#x60;. | [optional] 

## Example

```python
from openapi_client.models.checkout_option import CheckoutOption

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutOption from a JSON string
checkout_option_instance = CheckoutOption.from_json(json)
# print the JSON string representation of the object
print CheckoutOption.to_json()

# convert the object into a dict
checkout_option_dict = checkout_option_instance.to_dict()
# create an instance of CheckoutOption from a dict
checkout_option_form_dict = checkout_option.from_dict(checkout_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


