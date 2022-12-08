#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)
    print("Number of argument(s): ", num_args)

    if num_args > 1:
        for i in enumerate(sys.argv[1:], 1):
            print(i, ":", arg)

    else:
        print(":")
