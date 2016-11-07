#!/bin/python3

import sys


time = input().strip().split(":")
if ('AM' in time[2]):
    if (time[0] == '12'):
        print ("00"+":"+time[1]+":"+time[2][:2])
    else:
        print (time[0]+":"+time[1]+":"+time[2][:2])    
else:
    if(time[0]=='12'):
        print(str((int(time[0])))+":"+time[1]+":"+time[2][:2])
    else:
        print(str((int(time[0])+12))+":"+time[1]+":"+time[2][:2])
