#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1

    sequence = []


    while len(sequence) < length:
        sequence.append(a)
        a, b = b, a + b

    print(sequence)
    # return sequence
# print(print_fibonacci(9))