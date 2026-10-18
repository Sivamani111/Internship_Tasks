# Problem Name: Sherlock and the Valid String

# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    counts = list(freq.values())
    unique_counts = set(counts)

    if len(unique_counts) == 1:
        return "YES"

    if len(unique_counts) > 2:
        return "NO"

    a, b = sorted(unique_counts)

    if counts.count(a) == 1 and a == 1:
        return "YES"

    if counts.count(b) == 1 and b - a == 1:
        return "YES"

    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
