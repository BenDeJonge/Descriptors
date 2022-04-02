# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:27:49 2022

@author: dejong71
"""

#==============================================================================

class Descriptor:
    '''
    A parent descriptor class to control getting and setting of another
    class's attribute.

    Parameters
    ----------
    name : str
        The public name of the attribute.
    error_msg : str, optional
        The error message to print. The default is ''.
    check : callable, optional
        The data quality check to perform before setting the attribute.
        The default is lambda new_value : True.
    error_msg : str, optional
        The error message to print . 
        The default is 'The set value did not pass the check.'. 
    Returns
    -------
    None.
    '''  
    def __init__(self, 
                 name : str, 
                 check : callable=lambda new_value : True, 
                 error_msg : str='The set value did not pass the check.'):      
        self.public_name = name
        self.private_name = '_' + name
        self._check = check
        self._error_msg = error_msg
        
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)
    
    def __set__(self, obj, new_value : int):
        if self._check(new_value):
            setattr(obj, self.private_name, new_value)
        else:
            raise ValueError(self._error_msg)
            
#==============================================================================

class StrictlyPositiveIntegerDescriptor(Descriptor):
    '''
    A parent descriptor class to control getting and setting of another
    class's attribute.

    Parameters
    ----------
    name : str
        The public name of the attribute.
    check : bool, optional
        The data quality check to perform before setting the attribute.
        The default is True.
    error_msg : str, optional
        The error message to print . 
        The default is 'The set value did not pass the check.'.

    Returns
    -------
    None.
    '''
    def __init__(self, name : str):
        self.public_name = name
        self.private_name = '_' + name
        self._check = lambda x : isinstance(x, int) and x > 0
        self._error_msg =  f'Attribute {self.public_name} must be a strictly positive integer.'
        
#==============================================================================