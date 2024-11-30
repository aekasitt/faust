# ruff: noqa

from __future__ import annotations

# Standard Library Imports
from datetime import datetime
from pprint import pformat
from typing import Any, Literal

# Third Party Imports
from pydantic import AwareDatetime, BaseModel as PydanticBaseModel, ConfigDict
from pydantic.alias_generators import to_camel


def encode_datetime_z(dt: datetime) -> str:
    return dt.isoformat(timespec="microseconds").replace("+00:00", "Z")


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        # NOTE: json_encoders is deprecated. The right way to do it now is to define
        # an Annotated type with PlainSerializer defining custom serialization
        json_encoders={datetime: encode_datetime_z, AwareDatetime: encode_datetime_z},
        populate_by_name=True,
        protected_namespaces=(),
        alias_generator=to_camel,
    )

    def to_dict(
        self,
        mode: Literal["json", "python"] = "json",
        by_alias: bool = True,
        exclude_unset: bool = True,
        exclude_none: bool = True,
        **kwargs,
    ) -> dict[str, Any]:
        """Returns the model properties as a dict"""
        return self.model_dump(
            mode=mode,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_none=exclude_none,
            **kwargs,
        )

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pformat(self.to_dict())
