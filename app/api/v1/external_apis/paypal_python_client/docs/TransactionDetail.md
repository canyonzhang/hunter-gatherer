# TransactionDetail

The transaction details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_info** | [**TransactionInfo**](TransactionInfo.md) |  | [optional] 
**payer_info** | [**PayerInfo**](PayerInfo.md) |  | [optional] 
**shipping_info** | [**ShippingInfo**](ShippingInfo.md) |  | [optional] 
**cart_info** | [**CartInfo**](CartInfo.md) |  | [optional] 
**store_info** | [**StoreInfo**](StoreInfo.md) |  | [optional] 
**auction_info** | [**AuctionInfo**](AuctionInfo.md) |  | [optional] 
**incentive_info** | [**IncentiveInfo**](IncentiveInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_detail import TransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetail from a JSON string
transaction_detail_instance = TransactionDetail.from_json(json)
# print the JSON string representation of the object
print TransactionDetail.to_json()

# convert the object into a dict
transaction_detail_dict = transaction_detail_instance.to_dict()
# create an instance of TransactionDetail from a dict
transaction_detail_form_dict = transaction_detail.from_dict(transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


