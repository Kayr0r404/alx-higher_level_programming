#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 0:
        print("{} arguments.".format(argc))
    elif (argc == 1):
        print("{} argument:".format(argc))
        print("{}: ".format(argc + 1, sys.argv[sys.argv[0]]))
    else:
        print("{} argument:".format(argc))
        for i in range(argc):
            print("{}: ".format(argc + 1, sys.argv[i]))
