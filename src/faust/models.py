#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faust._compat import VALIDATOR

if VALIDATOR == "pydantic-v1":
  from faust._pydantic_v1.base_model import BaseModel  # noqa: F401
  from faust._pydantic_v1.models import *  # noqa: F403
elif VALIDATOR == "pydantic-v2":
  from faust._pydantic_v2.base_model import BaseModel
  from faust._pydantic_v2.models import *  # noqa: F403

__all__: tuple[str, ...] = ("BaseModel",)
