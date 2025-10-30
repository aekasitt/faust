import os


def getenv_defer_build() -> bool:
  # Support "0", "1", "false", "true", etc
  defer_build = os.getenv("MYMODELS_DEFER_BUILD")
  if defer_build is None:
    return None

  try:
    defer_build = int(defer_build)
  except ValueError:
    if defer_build.lower() == "true":
      return True
    if defer_build.lower() == "false":
      return False

  # Not sure what it is but it was defined so likely true
  return bool(defer_build)
