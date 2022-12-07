#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    for int in set(my_list):
        total += int

    return total
