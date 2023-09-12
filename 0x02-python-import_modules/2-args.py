#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    counter = len(argv)
    if counter == 1:
        print("0 arguments.")
    elif counter == 2:
        print("{:d} argument:".format(counter - 1))
    else:
        print("{:d} arguments:".format(counter - 1))
    
    for elm in range(1, counter):
        print("{:d}: {:s}".format((elm), argv[elm]))
