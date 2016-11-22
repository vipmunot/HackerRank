#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    x = [i for i in a if i <=0] 
    if(len(x)>=k):
        print('NO')
    else: print('YES')   