"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    str_time=s[:-2]
    str_flag=s[-2:]
    #time_lst=str_time.split(':')
    #hour=int(time_lst[0])
    hour = int(s[:2])
    hour_cov= hour+12 if str_flag=='PM'and hour!=12 else hour
    hour_cov= hour_cov-12 if str_flag=='AM'and hour==12 else hour_cov
    #time_cov=str(hour_cov).zfill(2)+':'+time_lst[1]+':'+time_lst[2]
    time_cov = str(hour_cov).zfill(2) + str_time[2:]
    return time_cov

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'time_output.txt'

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
