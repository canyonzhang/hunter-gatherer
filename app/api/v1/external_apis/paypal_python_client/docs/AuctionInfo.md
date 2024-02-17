# AuctionInfo

The auction information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auction_site** | **str** | The name of the auction site. | [optional] 
**auction_item_site** | **str** | The auction site URL. | [optional] 
**auction_buyer_id** | **str** | The ID of the buyer who makes the purchase in the auction. This ID might be different from the payer ID provided for the payment. | [optional] 
**auction_closing_date** | **str** | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The regular expression provides guidance but does not reject all invalid dates.&lt;/blockquote&gt; | [optional] 

## Example

```python
from openapi_client.models.auction_info import AuctionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AuctionInfo from a JSON string
auction_info_instance = AuctionInfo.from_json(json)
# print the JSON string representation of the object
print AuctionInfo.to_json()

# convert the object into a dict
auction_info_dict = auction_info_instance.to_dict()
# create an instance of AuctionInfo from a dict
auction_info_form_dict = auction_info.from_dict(auction_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


