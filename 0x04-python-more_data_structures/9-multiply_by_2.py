#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {}
    for i, j in a_dictionary.items():
        mult = j * 2
        new[i] = mult
    return new
