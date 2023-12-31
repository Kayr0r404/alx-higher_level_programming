#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()  # Using a set to store unique integers
    total_sum = 0

    for num in my_list:
        if num not in unique_integers:
            total_sum += num
            unique_integers.add(num)

    return (total_sum)
