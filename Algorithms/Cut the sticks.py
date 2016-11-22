#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = min(arr)
print(len(arr))
while (len(arr) >0):
    arr = [x - min(arr) for x in arr]
    arr = [x for x in arr if x!=0]
    if (len(arr) != 0):print(len(arr))