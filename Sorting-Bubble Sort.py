# -*- coding: utf-8 -*-
"""
@author: Vipul Munot
Python: 3
"""
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
def bubblesort(array):
    no_of_pass = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
                array[j],array[i] = array[i],array[j]
                no_of_pass +=1
    return (no_of_pass,array)
total,array = bubblesort(a)
print("Array is sorted in %s swaps."%total)
print("First Element: %s"%array[0])
print("Last Element: %s"%array[len(array)-1])

