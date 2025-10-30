from mymodels._compat import PYDANTIC_V2

if PYDANTIC_V2:
  from mymodels._pydantic_v2.base_model import BaseModel
  from mymodels._pydantic_v2.models import *  # noqa: F403

else:
  from mymodels._pydantic_v1.base_model import BaseModel  # noqa: F401
  from mymodels._pydantic_v1.models import *  # noqa: F403
