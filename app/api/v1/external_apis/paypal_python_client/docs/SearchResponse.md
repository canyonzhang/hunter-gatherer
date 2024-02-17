# SearchResponse

The search response information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_details** | [**List[TransactionDetail]**](TransactionDetail.md) | An array of transaction detail objects. | [optional] 
**account_number** | **str** | The merchant account number. | [optional] 
**start_date** | **str** | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The regular expression provides guidance but does not reject all invalid dates.&lt;/blockquote&gt; | [optional] 
**end_date** | **str** | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The regular expression provides guidance but does not reject all invalid dates.&lt;/blockquote&gt; | [optional] 
**last_refreshed_datetime** | **str** | The date and time, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6). Seconds are required while fractional seconds are optional.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The regular expression provides guidance but does not reject all invalid dates.&lt;/blockquote&gt; | [optional] 
**page** | **int** | A zero-relative index of transactions. | [optional] 
**total_items** | **int** | The total number of transactions as an integer beginning with the specified &#x60;page&#x60; in the full result and not just in this response. | [optional] 
**total_pages** | **int** | The total number of pages, as an &#x60;integer&#x60;, when the &#x60;total_items&#x60; is divided into pages of the specified &#x60;page_size&#x60;. | [optional] 
**links** | [**List[LinkDescription]**](LinkDescription.md) | An array of request-related [HATEOAS links](/api/rest/responses/#hateoas-links). | [optional] [readonly] 

## Example

```python
from openapi_client.models.search_response import SearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponse from a JSON string
search_response_instance = SearchResponse.from_json(json)
# print the JSON string representation of the object
print SearchResponse.to_json()

# convert the object into a dict
search_response_dict = search_response_instance.to_dict()
# create an instance of SearchResponse from a dict
search_response_form_dict = search_response.from_dict(search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


