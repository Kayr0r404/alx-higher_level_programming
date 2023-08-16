#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    for i in range(len(my_list)):
        if (my_list[i] == search):
            list.append(replace)
        else:
            list.append(my_list[i])
    return (list)
