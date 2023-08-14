#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in range(len(my_string)):
        if ((my_string[i] != chr(99)) and (my_string[i] != chr(67))):
            str += my_string[i]
    return (str)
