# ItemDetail

The item details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_code** | **str** | An item code that identifies a merchant&#39;s goods or service. | [optional] 
**item_name** | **str** | The item name. | [optional] 
**item_description** | **str** | The item description. | [optional] 
**item_options** | **str** | The item options. Describes option choices on the purchase of the item in some detail. | [optional] 
**item_quantity** | **str** | The number of purchased units of goods or a service. | [optional] 
**item_unit_price** | [**Money**](Money.md) |  | [optional] 
**item_amount** | [**Money**](Money.md) |  | [optional] 
**discount_amount** | [**Money**](Money.md) |  | [optional] 
**adjustment_amount** | [**Money**](Money.md) |  | [optional] 
**gift_wrap_amount** | [**Money**](Money.md) |  | [optional] 
**tax_percentage** | **str** | The percentage, as a fixed-point, signed decimal number. For example, define a 19.99% interest rate as &#x60;19.99&#x60;. | [optional] 
**tax_amounts** | [**List[ItemDetailTaxAmount]**](ItemDetailTaxAmount.md) | An array of tax amounts levied by a government on the purchase of goods or services. | [optional] 
**basic_shipping_amount** | [**Money**](Money.md) |  | [optional] 
**extra_shipping_amount** | [**Money**](Money.md) |  | [optional] 
**handling_amount** | [**Money**](Money.md) |  | [optional] 
**insurance_amount** | [**Money**](Money.md) |  | [optional] 
**total_item_amount** | [**Money**](Money.md) |  | [optional] 
**invoice_number** | **str** | The invoice number. An alphanumeric string that identifies a billing for a merchant. | [optional] 
**checkout_options** | [**List[CheckoutOption]**](CheckoutOption.md) | An array of checkout options. Each option has a name and value. | [optional] 

## Example

```python
from openapi_client.models.item_detail import ItemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDetail from a JSON string
item_detail_instance = ItemDetail.from_json(json)
# print the JSON string representation of the object
print ItemDetail.to_json()

# convert the object into a dict
item_detail_dict = item_detail_instance.to_dict()
# create an instance of ItemDetail from a dict
item_detail_form_dict = item_detail.from_dict(item_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


