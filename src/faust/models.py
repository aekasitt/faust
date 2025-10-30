#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faust._compat import PYDANTIC_V2

if PYDANTIC_V2:
  from faust._pydantic_v2.base_model import BaseModel
  from faust._pydantic_v2.models import *  # noqa: F403

else:
  from faust._pydantic_v1.base_model import BaseModel  # noqa: F401
  from faust._pydantic_v1.models import *  # noqa: F403
