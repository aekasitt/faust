#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard packages
from __future__ import annotations
import contextlib
from datetime import datetime
from pprint import pformat
from typing import Any

# Third-party packages
from pydantic import BaseConfig, validator
from pydantic import BaseModel as PydanticBaseModel

# Local modules
from faust._datetime import as_datetime_z


def encode_datetime_z(dt: datetime) -> str:
  return dt.isoformat(timespec="microseconds").replace("+00:00", "Z")


# Custom BaseModel class that applies json encoders to model fields.
#
# This ensures that the items of dict returned by `model.dict()` are fully serialized,
# which saves us from having to do `json.loads(model.json())`.
#
# Based on: https://github.com/pydantic/pydantic/issues/1409#issuecomment-1381655025
class BaseModel(PydanticBaseModel):
  class Config(BaseConfig):
    json_encoders = {datetime: encode_datetime_z}
    allow_population_by_field_name = True

  def _jsonable_iter(self, **kwargs):
    for key, value in super()._iter(**kwargs):
      yield key, self.__config__.json_encoders.get(type(value), lambda v: v)(value)

  @staticmethod
  @contextlib.contextmanager
  def jsonable_iter_patch():
    """Temporarily patch _iter method to yield json-serialiable values"""
    original_iter = BaseModel._iter
    BaseModel._iter = BaseModel._jsonable_iter
    yield
    BaseModel._iter = original_iter

  def to_dict(
    self,
    by_alias: bool = True,
    exclude_unset: bool = True,
    exclude_none: bool = True,
    **kwargs,
  ) -> dict:
    """Returns the model properties as a dict"""
    with self.jsonable_iter_patch():
      return self.dict(
        by_alias=by_alias, exclude_unset=exclude_unset, exclude_none=exclude_none, **kwargs
      )

  def to_str(self) -> str:
    """Returns the string representation of the model"""
    return pformat(self.to_dict())

  @validator("*")
  def check_datetime(cls, v: Any) -> Any:
    if isinstance(v, datetime):
      if v.tzinfo is None:
        raise AssertionError("Datetimes must contain timezone offset")
      v = as_datetime_z(v)
    return v
