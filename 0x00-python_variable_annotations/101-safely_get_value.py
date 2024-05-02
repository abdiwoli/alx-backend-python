#!/usr/bin/env python3
""" advanced tasks """
from typing import Iterable, Sequence, List, Tuple, Any, Union, Mapping, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar(
        'T'), None] = None) -> Union[TypeVar('T'), type(None)]:
    if key in dct:
        return dct[key]
    else:
        return default
