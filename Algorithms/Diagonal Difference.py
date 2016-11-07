#!/bin/python3

import sys


N = int(input())
difference = 0
for i in range(N):
    row = input().split()
    print(row)
    print(row[i])
    print(row[N-1-i])
    difference += (int(row[i]) - int(row[N-1-i]))
print (abs(difference) )