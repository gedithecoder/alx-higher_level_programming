#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    num1 = int(sys.argv[1])
    sign = sys.argv[2]
    num2 = int(sys.argv[3])
    count = len(sys.argv) - 1

    if sign == "+":
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif sign == "-":
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
    elif sign == "*":
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif sign == "/":
        print("{} / {} = {}".format(num1, num2, div(num1, num2)))
    elif sign != "+" or sign != "-" or sign != "*" or sign != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
