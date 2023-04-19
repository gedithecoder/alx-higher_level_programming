#!/usr/bin/python3

def search_replace(my_list, search, replace):
    indices = []
    for idx, value in enumerate(my_list):
        if value == search:
            indices.append(idx)
    new_list = my_list[:]
    for i in indices:
        new_list[i] = replace

    return new_list
