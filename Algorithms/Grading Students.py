#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    # your code goes here
    if grade > 37:
        rem=grade%10
        if rem == 3 or rem == 8:
            grade+=2
        elif rem ==4 or rem == 9:
            grade+=1
    print (grade)
