#!/usr/bin/env python3
def no_c(my_string):
    for i in my_string:
        if my_string[i] == c or my_string[i] == C:
            del(my_string[i])
    return my_string
