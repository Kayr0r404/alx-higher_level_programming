#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx > (len(my_list) -1) or idx < 0):
        return (my_list)
    else:
        newList = []
        for i in range(len(my_list)):
            if (i != idx):
                newList.append(my_list[i])
            else:
                continue
        return (newList)