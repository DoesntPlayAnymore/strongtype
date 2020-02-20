from functools import wraps
from typing import NamedTuple




def typedtuple(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        for c in cls.__bases__:
            types = cls._field_types
            for arg, t in zip(args, types.values()):
                if not isinstance(arg, t):
                    raise TypeError(f'Expected {t}, got {type(arg)}.')
        return cls
    return wrapper



def typedtuplemerge(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        fields = []
        for c in cls.__bases__:
            types = cls._field_types
            for arg, t in zip(args, types.values()):
                if not isinstance(arg, t):
                    raise TypeError(f'Expected {t}, got {type(arg)}.')
            fields.extend(tuple(types.items()))
        return NamedTuple(cls.__name__, fields)(*args, **kwargs)
    return wrapper