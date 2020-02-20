from dataclasses import dataclass



@dataclass
class StronglyTyped:
    """
    Base class for all strongly typed dataclasses.
    
    Inheriting dataclasses will be strongly typed, meaning 
    they cannot be initialized with parameters that conflict
    with their annotated types.
    
    Inheriting classes must be annotated with @dataclasses.dataclass
    and use proper type annotations as according to the dataclasses
    documentation.
        See: https://docs.python.org/3/library/dataclasses.html
        
    Examples:
    ---------
    >>> @dataclass
    ... class X(StronglyTyped):
    ...    x: int
    
    >>> x = X('1')
    TypeError: Expected type <class 'int'>, recieved <class 'str'>
    """
    def __setattr__(self, name, value):
        types = self.__annotations__
        
        if name in types and not isinstance(
                value, 
                types[name]
        ):
            raise TypeError(
                    f'Expected type {types[name]}, recieved {type(value)}'
            )
        return super().__setattr__(name, value)
