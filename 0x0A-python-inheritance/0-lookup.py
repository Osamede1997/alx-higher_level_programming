#!/usr/bin/python3

"""Defines an object lookup function"""


def lookup(obj):
    """Returns the list of attributes and methods"""
    return (dir(obj))
