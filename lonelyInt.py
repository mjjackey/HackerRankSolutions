"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
Given an array of integers, where all elements but one occur twice, find the unique element.

Example

The unique element is .

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
Input Format

The first line contains a single integer, , the number of integers in the array.
The second line contains  space-separated integers that describe the values in .

Constraints

It is guaranteed that  is an odd number and that there is one unique element.
, where .
"""

#!/bin/python3

from itertools import count
from collections import Counter

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    b = sorted(a)
    n = len(b)
    i = 0
    while i < n:
        if i == n - 1:
            return b[n - 1]
        elif i < n - 1:
            if b[i] == b[i + 1]:
                i += 2
            else:
                return b[i]

def lonelyinteger2(a):
    b=[0]*n
    for i in range(len(a)):
        b[i]=a.count(a[i])
        i+=1
    for j in range(len(b)):
        if b[j]==1: return a[j]

def lonelyinteger3(a):
   b=Counter(a)
   num=[k for k,v in b.items() if v==1]
   return num[0]

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'lonelyInt_output.txt'

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger3(a)

    fptr.write(str(result) + '\n')

    fptr.close()
