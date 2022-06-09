#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):                                                                      
    newDict = list(a_dictionary.key())
    newDict.sort()
    for i in newDict:
        print("{}: {}".format(i, a_dictionary.get(i)))
