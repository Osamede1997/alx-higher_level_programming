#!/usr/bin/python3

"""Defines a file opener function"""


def read_file(filename=""):
    """file function"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
