#!/usr/bin/python3
"""implementation"""


def say_my_name(first_name, last_name=""):
    """
     a function that prints My name is <first name> <last name>

     first_name and last_name must be strings otherwise, raise a
     TypeError exception with the message first_name must be a
     string or last_name must be a strin
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    # if (len(first_name) == 0 and last_name == ""):
    #     print("")
    # else:
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
