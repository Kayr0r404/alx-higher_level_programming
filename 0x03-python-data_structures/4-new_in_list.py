#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if ((len(my_list) - 1 < idx) or (idx < 0)):
        return (my_list.copy())
    else:
        newList = my_list.copy()
        newList[idx] = element
        return (newList)
