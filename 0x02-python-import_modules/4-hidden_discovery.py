#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for i in range(len(list)):
        str = list[i]
        if (str[0] != '_'):
            print("{}".format(str))
