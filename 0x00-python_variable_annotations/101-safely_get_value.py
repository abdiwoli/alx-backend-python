#!/usr/bin/env python3
""" adavanced anotation 101-safely_get_value.py documen """
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """ function saveley get value
        hello
     """
    if key in dct:
        return dct[key]
    else:
        return default
