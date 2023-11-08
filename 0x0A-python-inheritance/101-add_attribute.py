#!/usr/bin/python3
''' add_attribute function ''''


def add_attribute(obj, name, value):
    ''' function that adds a new attribute
        to an object if it’s possible
    '''
    if isinstance(obj, (int, float, str, tuple, bool, dict, frozenset)):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
