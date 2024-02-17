# PayerInfo

The payer information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The PayPal&#x60; customer account ID. | [optional] 
**email_address** | **str** | The internationalized email address.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; Up to 64 characters are allowed before and 255 characters are allowed after the &lt;code&gt;@&lt;/code&gt; sign. However, the generally accepted maximum length for an email address is 254 characters. The pattern verifies that an unquoted &lt;code&gt;@&lt;/code&gt; sign exists.&lt;/blockquote&gt; | [optional] 
**phone_number** | [**Phone**](Phone.md) |  | [optional] 
**address_status** | **str** | The address status of the payer. Value is either:&lt;ul&gt;&lt;li&gt;&lt;code&gt;Y&lt;/code&gt;. Verified.&lt;/li&gt;&lt;li&gt;&lt;code&gt;N&lt;/code&gt;. Not verified.&lt;/li&gt;&lt;/ul&gt; | [optional] 
**payer_status** | **str** | The status of the payer. Value is &#x60;Y&#x60; or &#x60;N&#x60;. | [optional] 
**payer_name** | [**Name**](Name.md) |  | [optional] 
**country_code** | **str** | The [two-character ISO 3166-1 code](/docs/integration/direct/rest/country-codes/) that identifies the country or region.&lt;blockquote&gt;&lt;strong&gt;Note:&lt;/strong&gt; The country code for Great Britain is &lt;code&gt;GB&lt;/code&gt; and not &lt;code&gt;UK&lt;/code&gt; as used in the top-level domain names for that country. Use the &#x60;C2&#x60; country code for China worldwide for comparable uncontrolled price (CUP) method, bank card, and cross-border transactions.&lt;/blockquote&gt; | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from openapi_client.models.payer_info import PayerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayerInfo from a JSON string
payer_info_instance = PayerInfo.from_json(json)
# print the JSON string representation of the object
print PayerInfo.to_json()

# convert the object into a dict
payer_info_dict = payer_info_instance.to_dict()
# create an instance of PayerInfo from a dict
payer_info_form_dict = payer_info.from_dict(payer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


