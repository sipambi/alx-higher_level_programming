#!/usr/bin/python3
def uniq_add(my_list=[]):
    theList = set(my_list)
    x = 0

    for i in theList:
        x = x + i
    return x
