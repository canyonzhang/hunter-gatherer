# coding: utf-8

"""
    Transaction Search

    Use the Transaction Search API to get the history of transactions for a PayPal account. To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>. For more information about the API, see the <a href=\"/docs/transaction-search/\">Transaction Search API Integration Guide</a>.<blockquote><strong>Note:</strong> To use the API on behalf of third parties, you must be part of the PayPal partner network. Reach out to your partner manager for the next steps. To enroll in the partner program, see <a href=\"https://www.paypal.com/my/webapps/mpp/partner-program/global-programs\">Partner with PayPal</a>.</blockquote>

    The version of the OpenAPI document: 1.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.error_link_description import ErrorLinkDescription
from typing import Optional, Set
from typing_extensions import Self

class Error500(BaseModel):
    """
    This is either a system or application error, and generally indicates that although the client appeared to provide a correct request, something unexpected has gone wrong on the server.
    """ # noqa: E501
    name: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    debug_id: Optional[StrictStr] = Field(default=None, description="The PayPal internal ID. Used for correlation purposes.")
    links: Optional[Annotated[List[ErrorLinkDescription], Field(min_length=0, max_length=10000)]] = Field(default=None, description="An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).")
    __properties: ClassVar[List[str]] = ["name", "message", "debug_id", "links"]

    @field_validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INTERNAL_SERVER_ERROR']):
            raise ValueError("must be one of enum values ('INTERNAL_SERVER_ERROR')")
        return value

    @field_validator('message')
    def message_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['An internal server error occurred.']):
            raise ValueError("must be one of enum values ('An internal server error occurred.')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Error500 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Error500 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "message": obj.get("message"),
            "debug_id": obj.get("debug_id"),
            "links": [ErrorLinkDescription.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj

