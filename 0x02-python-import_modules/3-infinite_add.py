#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv[1:]) == 0:
        print("0")
    elif len(argv) >= 1:
        int_list = [int(args) for args in argv[1:]]
        print(sum(int_list))
