#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
max_num = 0
for x in a:
    temp = a.count(x) + a.count(x+1)
    if temp > max_num:
        max_num = temp
print(max_num)