# CartInfo

The cart information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_details** | [**List[ItemDetail]**](ItemDetail.md) | An array of item details. | [optional] 
**tax_inclusive** | **bool** | Indicates whether the item amount or the shipping amount already includes tax. | [optional] [default to False]
**paypal_invoice_id** | **str** | The ID of the invoice. Appears for only PayPal-generated invoices. | [optional] 

## Example

```python
from openapi_client.models.cart_info import CartInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CartInfo from a JSON string
cart_info_instance = CartInfo.from_json(json)
# print the JSON string representation of the object
print CartInfo.to_json()

# convert the object into a dict
cart_info_dict = cart_info_instance.to_dict()
# create an instance of CartInfo from a dict
cart_info_form_dict = cart_info.from_dict(cart_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


