#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    k = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for j in new_list:
        k += j
    return k

