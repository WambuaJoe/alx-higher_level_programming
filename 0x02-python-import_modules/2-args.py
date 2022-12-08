#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv)
    if num_args == 1:
        print("No arguments were passed.")
    elif num_args == 2:
        print("One argument was passed: ")
    else:
        print(f"{num_args} arguments were passed: ")

    for i in range(1, num_args):
        print(f"{i}: {argv[i]}")
