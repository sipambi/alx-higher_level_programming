#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):                                                                      
    newDict = sorted(a_dictionary)                                                                                          
    for i in newDict:
        print("{}: {}".format(i, a_dictionary.get(i)))
