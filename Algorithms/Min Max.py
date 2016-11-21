#!/bin/python

import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
lst=[a,b,c,d,e]
s=[]
for i in range(len(lst)):
    r=lst[:i]+lst[i+1:]
    s.append(sum(r))
print(min(s),max(s))
