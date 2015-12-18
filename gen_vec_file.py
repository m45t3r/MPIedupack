#!/usr/bin/python3

import random
import sys

try:
    p = sys.argv[1]
except IndexError:
    p = input("Number of processors: ")
p = int(p)

try:
    n = sys.argv[2]
except IndexError:
    n = input("How many numbers: ")
n = int(n)

try:
    filename = sys.argv[3]
except IndexError:
    filename = input("Filename: ")

with open(filename, mode='w') as f:
    f.write("{0} {1}\n".format(n, p))
    for i in range(1, n + 1):
        f.write("{0} {1}\n".format(i, random.randint(1, p)))
