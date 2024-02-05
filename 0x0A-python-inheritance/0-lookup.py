#!/usr/bin/python3
'''Module for lookup method'''

def lookup(obj):
    '''function looks up attributes and methods of an object.
    Args:
        obj (object): object to list.
    Returns:
        list: list of attributes.
    '''
    return dir(obj)
