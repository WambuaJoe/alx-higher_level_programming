#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)
    print("Number of argument(s): ", num_args)

    if num_args > 1:
        for i in range(1, num_args):
            print(i, ":", sys.argv[1])

    else:
        print(":")
