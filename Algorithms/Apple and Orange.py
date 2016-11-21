#!/bin/python3

import sys

def dist(a,value):
    return (a+value)

    
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
ap_cnt = 0
for i in range(len(apple)):
    d = dist(a,apple[i])
    if (d >= s and d<=t):
        ap_cnt +=1
print(ap_cnt)        
or_cnt = 0
for i in range(len(orange)):
    d = dist(b,orange[i])
    if (d >= s and d<=t):
        or_cnt +=1
print(or_cnt)        