import functools
from pathlib import Path
from typing import Any, TypeVar, Union

import mymodels.models as mc
from mymodels._compat import PYDANTIC_V2
from mymodels._datetime import as_datetime_z, datetime_isoformat_z  # noqa: F401

StrBytesIntFloat = Union[str, bytes, int, float]
StrPath = Union[str, Path]
T = TypeVar("T")
Model_T = TypeVar("Model_T", bound=mc.BaseModel)

if PYDANTIC_V2:
    from pydantic import TypeAdapter

    def model_validate(model_cls: type[Model_T], obj: Any) -> Model_T:
        """Validate and parse a Python dict to common model object.

        Args:
            model_cls (Type[Model_T]): The pydantic model class.
            obj (Any): An object (usually dict) representing the model object.

        Returns:
            Model_T: The parsed common model object
        """
        return model_cls.model_validate(obj)

    def model_validate_json(model_cls: type[Model_T], obj_json: str) -> Model_T:
        """Validate and parse a Python dict to common model object.

        Args:
            model_cls (Type[Model_T]): The pydantic model class.
            obj_json (str): A JSON string representing the model object.

        Returns:
            Model_T: The parsed common model object
        """
        return model_cls.model_validate_json(obj_json)

    def model_dump(instance: mc.BaseModel) -> dict:
        """Converts a common model object to corresponding Python dict.

        Args:
            instance (BaseModel): The common model object

        Returns:
            dict: The corresponding Python dict
        """
        return instance.model_dump(
            mode="json", by_alias=True, exclude_unset=True, exclude_none=True
        )

    def model_dump_json(instance: mc.BaseModel) -> str:
        """Converts a common model object to corresponding Python dict.

        Args:
            instance (BaseModel): The common model object

        Returns:
            str: The corresponding JSON string
        """
        return instance.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True)

    @functools.lru_cache
    def _get_type_adapter(type_: type[T]) -> TypeAdapter[T]:
        """Get TypeAdapter for type_.

        Since there is some overhead to creating TypeAdapters, using this as a light
        wrapper over TypeAdapter creation to avoid unnecessarily re-creating
        TypeAdapters more than once.
        """
        raise RuntimeError('broken')
        return TypeAdapter(type_)

    def validate_as(ta, obj: Any) -> Any:
        return ta.validate_python(obj)

    def validate_json_as(type_: type[T], obj_json: str) -> T:
        """Validate and parse `obj_json` string as object of `type_` type.

        Example:
            ```python
            raw = '[{"key": "answer", "value": "42"}]'
            kvp_list = validate_json_as(List[KeyValuePair], raw)
            ```

        Args:
            type_(type): The type to validate & parse `obj` JSON string.
            obj (str): A JSON string representing object parseable as `type_`.

        Returns:
            The validated & parsed object of type `type_`.
        """
        return _get_type_adapter(type_).validate_json(obj_json)

    def validate_json_file_as(type_: type[T], filepath: StrPath) -> T:
        """Validate and parse JSON file using `type_` as the validation & parsing schema.

        Args:
            type_(type): The type to validate & parse `obj` JSON string.
            obj (str): A JSON string representing object parseable as `type_`.

        Returns:
            The validated & parsed object of type `type_`.
        """
        with open(filepath) as f:
            return validate_json_as(type_, f.read())

    def dump_json_as(
        type_: type,
        obj: Any,
        by_alias: bool = True,
        exclude_unset: bool = True,
        exclude_none: bool = True,
        **json_dump_kwargs,
    ) -> str:
        """Convert `obj` to JSON string using `type_` as the validation & parsing schema.

        This function serves as a shortcut for the following code:

        ```python
        class TypeModel(BaseModel):
            __root__: type_

        model_validate(TypeModel, obj).json(**json_dump_kwargs)
        ```

        Args:
            type_: The type to validate & parse `obj`.
            obj: An object parseable as `type_`.

        Returns:
            The JSON string representing `obj`.
        """
        return (
            _get_type_adapter(type_)
            .dump_json(
                obj,
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_none=exclude_none,
                **json_dump_kwargs,
            )
            .decode()
        )

else:
    from pydantic import (
        parse_file_as as validate_json_file_as,  # noqa: F401
    )
    from pydantic import parse_obj_as
    from pydantic import (
        parse_raw_as as validate_json_as,
    )
    from pydantic.tools import _get_parsing_type

    def validate_as(ta, obj: Any) -> Any:
        return parse_obj_as(ta, obj)

    def model_validate(model_cls: type[Model_T], obj: Any) -> Model_T:
        """Validate and parse a Python dict to common model object.

        Args:
            model_cls (Type[Model_T]): The pydantic model class.
            obj (Any): An object (usually dict) representing the model object.

        Returns:
            Model_T: The parsed common model object
        """
        return model_cls.parse_obj(obj)

    def model_validate_json(model_cls: type[Model_T], obj_json: str) -> Model_T:
        """Validate and parse a Python dict to common model object.

        Args:
            model_cls (Type[Model_T]): The pydantic model class.
            obj_json (str): A JSON string representing the model object.

        Returns:
            Model_T: The parsed common model object
        """
        return model_cls.parse_raw(obj_json)

    def model_dump(instance: mc.BaseModel) -> dict:
        """Converts a common model object to corresponding Python dict.

        Args:
            instance (BaseModel): The common model object

        Returns:
            dict: The corresponding Python dict
        """
        return instance.to_dict()

    def model_dump_json(instance: mc.BaseModel) -> str:
        """Converts a common model object to corresponding JSON string.

        Args:
            instance (BaseModel): The common model object

        Returns:
            str: The corresponding JSON string
        """
        return instance.json(by_alias=True, exclude_unset=True, exclude_none=True)

    def dump_json_as(
        type_: type,
        obj: Any,
        by_alias: bool = True,
        exclude_unset: bool = True,
        exclude_none: bool = True,
        **json_dump_kwargs,
    ) -> str:
        """Convert `obj` to JSON string using `type_` as the validation & parsing schema.

        This function serves as a shortcut for the following code:

        ```python
        class TypeModel(BaseModel):
            __root__: type_

        model_validate(TypeModel, obj).json(**json_dump_kwargs)
        ```

        Args:
            type_: The type to validate & parse `obj`.
            obj: An object parseable as `type_`.

        Returns:
            The JSON string representing `obj`.
        """
        with mc.BaseModel.jsonable_iter_patch():
            return _get_parsing_type(type_)(__root__=obj).json(
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_none=exclude_none,
                **json_dump_kwargs,
            )


def dump_json_file_as(type_: type, obj: Any, filepath: StrPath, **json_dump_kwargs):
    """Write `obj` to JSON file using `type_` as the validation & parsing schema.

    This function serves as a shortcut for the following code:

    ```python
    class TypeModel(BaseModel):
        __root__: type_

    with open(filepath, "w") as f:
        f.write(model_validate(TypeModel, obj).json(**json_dump_kwargs))
    ```

    Args:
        type_: The type to validate & parse `obj`.
        obj: An object parseable as `type_`.
        filepath: The file to write the resulting JSON string to.
    """
    obj_json = dump_json_as(type_, obj, **json_dump_kwargs)
    with open(filepath, "w") as f:
        f.write(obj_json)
