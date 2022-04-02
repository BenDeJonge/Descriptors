# Descriptors
Simple descriptors to handle getting and setting of class attributes. More information can be found in the [Python documentation](https://docs.python.org/3/howto/descriptor.html).

A descriptor can be added to any class as follows:
```
class Class:   
    #---DESCRIPTORS------------------------------------------------------------
    
    arg1 = StrictlyPositiveIntegerDescriptor('arg1')
    arg2 = StrictlyPositiveIntegerDescriptor('arg2')
    
    #---INITIALIZATION---------------------------------------------------------

    def __init__(self, arg1 : int, arg2 : int):
        self.arg1 = arg1
        self.arg1 = arg1
```

## Descriptor
Base class to get and set attributes.

## StrictlyPositiveIntegerDescriptor
Enforce attribute to be a strictly positive integer.
