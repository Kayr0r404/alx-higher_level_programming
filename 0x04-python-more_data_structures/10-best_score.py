#!/usr/bin/python3
def best_score(a_dictionary):
    maxi, maxiKey = None, None

    if (a_dictionary is None):
        return None
    for key, value in a_dictionary.items():
        if maxi is None or value > maxi:
            maxi = value
            maxiKey = key
    return maxiKey
