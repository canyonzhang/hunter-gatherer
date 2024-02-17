# ItemDetailTaxAmount

The tax levied by a government on the purchase of goods or services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_amount** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_detail_tax_amount import ItemDetailTaxAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDetailTaxAmount from a JSON string
item_detail_tax_amount_instance = ItemDetailTaxAmount.from_json(json)
# print the JSON string representation of the object
print ItemDetailTaxAmount.to_json()

# convert the object into a dict
item_detail_tax_amount_dict = item_detail_tax_amount_instance.to_dict()
# create an instance of ItemDetailTaxAmount from a dict
item_detail_tax_amount_form_dict = item_detail_tax_amount.from_dict(item_detail_tax_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


