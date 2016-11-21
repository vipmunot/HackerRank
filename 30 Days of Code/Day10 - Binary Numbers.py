#!/bin/python3

import sys


print(len(max(bin(int(input().strip()))[2:].split('0'))))