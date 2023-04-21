#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for i, j in a_dictionary.items():
        if bool(a_dictionary) ==  False:
            a_dictionary[key] = value
            break
        elif i == key:
            a_dictionary[i] = value
        else:
            a_dictionary[key] = value

        return a_dictionary
