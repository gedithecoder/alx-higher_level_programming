#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for i, j in a_dictionary.items():
        mult = j * 2
        a_dictionary[i] = mult
    return a_dictionary
