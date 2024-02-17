# Name

The name of the party.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The prefix, or title, to the party&#39;s name. | [optional] 
**given_name** | **str** | When the party is a person, the party&#39;s given, or first, name. | [optional] 
**surname** | **str** | When the party is a person, the party&#39;s surname or family name. Also known as the last name. Required when the party is a person. Use also to store multiple surnames including the matronymic, or mother&#39;s, surname. | [optional] 
**middle_name** | **str** | When the party is a person, the party&#39;s middle name. Use also to store multiple middle names including the patronymic, or father&#39;s, middle name. | [optional] 
**suffix** | **str** | The suffix for the party&#39;s name. | [optional] 
**alternate_full_name** | **str** | DEPRECATED. The party&#39;s alternate name. Can be a business name, nickname, or any other name that cannot be split into first, last name. Required when the party is a business. | [optional] 
**full_name** | **str** | When the party is a person, the party&#39;s full name. | [optional] 

## Example

```python
from openapi_client.models.name import Name

# TODO update the JSON string below
json = "{}"
# create an instance of Name from a JSON string
name_instance = Name.from_json(json)
# print the JSON string representation of the object
print Name.to_json()

# convert the object into a dict
name_dict = name_instance.to_dict()
# create an instance of Name from a dict
name_form_dict = name.from_dict(name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


