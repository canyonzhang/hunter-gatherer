# ErrorLinkDescription

The request-related [HATEOAS link](/api/rest/responses/#hateoas-links) information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The complete target URL. To make the related call, combine the method with this [URI Template-formatted](https://tools.ietf.org/html/rfc6570) link. For pre-processing, include the &#x60;$&#x60;, &#x60;(&#x60;, and &#x60;)&#x60; characters. The &#x60;href&#x60; is the key HATEOAS component that links a completed call with a subsequent call. | 
**rel** | **str** | The [link relation type](https://tools.ietf.org/html/rfc5988#section-4), which serves as an ID for a link that unambiguously describes the semantics of the link. See [Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml). | 
**method** | **str** | The HTTP method required to make the related call. | [optional] 

## Example

```python
from openapi_client.models.error_link_description import ErrorLinkDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorLinkDescription from a JSON string
error_link_description_instance = ErrorLinkDescription.from_json(json)
# print the JSON string representation of the object
print ErrorLinkDescription.to_json()

# convert the object into a dict
error_link_description_dict = error_link_description_instance.to_dict()
# create an instance of ErrorLinkDescription from a dict
error_link_description_form_dict = error_link_description.from_dict(error_link_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


