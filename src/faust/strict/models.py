from mymodels._compat import PYDANTIC_V2

if PYDANTIC_V2:
  from mymodels._pydantic_v2.strict.models import *  # noqa: F403
else:
  from mymodels._pydantic_v1.strict.models import *  # noqa: F403
