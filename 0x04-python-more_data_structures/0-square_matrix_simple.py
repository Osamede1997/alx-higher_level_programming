#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for row in matrix:
        return ([list(map(lambda x: x * x, row)) for row in matrix])

#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
