# LinkDescription

The request-related [HATEOAS link](/docs/api/reference/api-responses/#hateoas-links) information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The complete target URL. To make the related call, combine the method with this [URI Template-formatted](https://tools.ietf.org/html/rfc6570) link. For pre-processing, include the &#x60;$&#x60;, &#x60;(&#x60;, and &#x60;)&#x60; characters. The &#x60;href&#x60; is the key HATEOAS component that links a completed call with a subsequent call. | 
**rel** | **str** | The [link relation type](https://tools.ietf.org/html/rfc5988#section-4), which serves as an ID for a link that unambiguously describes the semantics of the link. See [Link Relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml). | 
**method** | **str** | The HTTP method required to make the related call. | [optional] 

## Example

```python
from openapi_client.models.link_description import LinkDescription

# TODO update the JSON string below
json = "{}"
# create an instance of LinkDescription from a JSON string
link_description_instance = LinkDescription.from_json(json)
# print the JSON string representation of the object
print LinkDescription.to_json()

# convert the object into a dict
link_description_dict = link_description_instance.to_dict()
# create an instance of LinkDescription from a dict
link_description_form_dict = link_description.from_dict(link_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


