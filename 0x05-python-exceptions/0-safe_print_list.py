#!/usr/bin/python3
returnValue = 0
def safe_print_list(my_list=[], x=0):
    for a in range(x):
        try:
            print (my_list[a], end="")
            returnValue = a + 1
        except IndexError:
            break
    print ("")
    return (returnValue)
