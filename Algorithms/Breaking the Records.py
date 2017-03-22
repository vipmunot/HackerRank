#!/bin/python3

import sys


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
# your code goes here
maxval = score[0]
minval = score[0]
maxcnt,mincnt = 0,0

for item in score:
    if item > maxval:
        maxval = item
        maxcnt +=1
    elif item < minval:
        minval = item
        mincnt +=1
    else:
        continue
print(maxcnt,mincnt) 
