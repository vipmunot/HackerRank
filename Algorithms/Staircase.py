#!/bin/python3

import sys

space = []
string = []
n = int(input().strip())
for i in range(1,n+1):
    string.append(i*"#")
for j in range(n-1,-1,-1):
    space.append(j*" ")
for i in range(len(string)):
    print(space[i]+string[i])