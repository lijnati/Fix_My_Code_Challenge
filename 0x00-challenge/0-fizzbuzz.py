#!/usr/bin/python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    result = ""
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz "
        elif i % 3 == 0:
            result += "Fizz "
        elif i % 5 == 0:
            result += "Buzz "
        else:
            result += str(i) + " "
    return result.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-fizzbuzz.py <number>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    print(fizzbuzz(n))
