# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:00:09 2016

@author: Nikolay
"""
import numpy as np

#tosort = [5, 2, 0, 10, 12, 44, -5, 192, 0.001, -0.0001, 1000]
tosort = np.random.randint(-1000, 1000, 1000)

def merge(left, right):
    result = []
    while (len(left) > 0) & (len(right) > 0):
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    for i in left:
        result.append(i)
    for i in right:
        result.append(i)
    return result
    
def merge_sort(m):
    if len(m) <= 1:
        return m
    left = []
    right = []
    for i in range(len(m)):
        if i % 2 == 0:
            left.append(m[i])
        else:
            right.append(m[i])
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    

print(merge_sort(tosort))

#import time
#t0 = time.clock()
##merge_sort(tosort)
#sorted(tosort)
#print(time.clock() - t0)