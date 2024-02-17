# ShippingInfo

The shipping information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The recipient&#39;s name. | [optional] 
**method** | **str** | The shipping method that is associated with this order. | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**secondary_shipping_address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_info import ShippingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingInfo from a JSON string
shipping_info_instance = ShippingInfo.from_json(json)
# print the JSON string representation of the object
print ShippingInfo.to_json()

# convert the object into a dict
shipping_info_dict = shipping_info_instance.to_dict()
# create an instance of ShippingInfo from a dict
shipping_info_form_dict = shipping_info.from_dict(shipping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


