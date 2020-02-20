from dataclasses import dataclass



@dataclass
class ImmutableTyped:
    """
    Base class for all strongly typed, immutable dataclasses.
    
    Inheriting dataclasses will be immutable and strongly typed, 
    meaning they cannot have their values changed after initialization 
    and cannot be initialized with parameters that conflict with their 
    annotated types.
    
    Inheriting classes must be annotated with @dataclasses.dataclass
    and use proper type annotations as according to the dataclasses
    documentation.
        See: https://docs.python.org/3/library/dataclasses.html
        
    Examples:
    ---------
    >>> @dataclass
    ... class X(ImmutableTyped):
    ...    x: int
    
    >>> x = X('1')
    TypeError: Expected type <class 'int'>, recieved <class 'str'>

    >>> x = X(1)
    >>> x.x = 5
    AttributeError: Attempted to set attribute 'x' on immutable class <class '__main__.X'>.
    """
    def __post_init__(self):
        """
        Sets immutable flag to True after initialization.
        """
        self._immutable = True

    def __setattr__(self, name, value):
        if not '_immutable' in self.__dict__:
            types = self.__annotations__
            
            if name in types and not isinstance(
                    value, 
                    types[name]
            ):
                raise TypeError(
                        f'Expected type {types["name"]}, recieved {type(value)}'
                )
            return super().__setattr__(name, value)
        else:
            raise AttributeError(f'Attempted to set attribute {name} on immutable class {self.__class__}.')
