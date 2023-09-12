#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    operators = ['+', '-', '*', '/']
    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if argv[2] == '+':
                print("{} + {} = {}".format(argv[1], argv[3],
                                            sum(int(argv[1], argv[3]))))
