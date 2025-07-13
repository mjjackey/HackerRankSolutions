#!/bin/python3
"""
STDIN                Function
-----                --------
6               →    logs[] size n = 6
99 1 sign-in    →    logs = ["99 1 sign-in","100 10 sign-in","50 20 sign-in","100 15 sign-out","50 26 sign-out","99 2 sign-out"]
100 10 sign-in
50 20 sign-in
100 15 sign-out
50 26 sign-out
99 2 sign-out
5               →    maxSpan = 5

Output:
100
50
"""

import math
import os
import random
import re
import sys


#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs:list, maxSpan:int)-> list:
    # Write your code here
    user_ids = []

    for lon_info in logs:
        log_info_strs = lon_info.split(" ")
        if (len(log_info_strs) == 3):
            user_ids.append(log_info_strs[0])
        else:
            print("Invalid log format: ", lon_info)
            exit(1)

    user_ids_set = set(user_ids)
    log_item_list = []
    log_item_info_dict = {}
    for id in user_ids_set:
        log_time_dict = {"sign-in":None, "sign-out":None}  # Set to store sign-in and sign-out times
        if id not in log_item_info_dict.keys():
            log_item_info_dict[id]=log_time_dict # Add user ID to the log item info
        else:
            log_time_dict = log_item_info_dict[id]  # Get the existing dict for this user ID
        for log_info in logs:
            log_info_strs = log_info.split(" ")
            if id in log_info_strs:
                if "sign-in" in log_info_strs:
                    sign_in_time = int(log_info_strs[1])
                    log_time_dict["sign-in"]=sign_in_time
                elif "sign-out" in log_info_strs:
                    sign_out_time = int(log_info_strs[1])
                    log_time_dict["sign-out"]=sign_out_time
        log_item_list.append([id,log_item_info_dict[id]["sign-in"], log_item_info_dict[id]["sign-out"]])
    sorted(log_item_list, key=lambda x: x[2]-x[1])  # Sort by the time difference
    log_times = filter(lambda x: (x[2] - x[1]) >= maxSpan, log_item_list)  # Filter by maxSpan
    result = [next(iter(s)) for s in log_times]
    return result


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'  # Set output path for testing
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # input number
    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()