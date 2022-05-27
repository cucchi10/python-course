

from itertools import count
import math
import os
import random
import re
import sys

'''
def miniMaxSum(arr):
    minsum = sum(arr) - max(arr)
    maxsum = sum(arr) - min(arr)
    
    print(minsum, maxsum)
'''

def miniMaxSum(arr):
    arr = sorted(arr)
    arrs = -1
    sumatotal=0

    for a in arr:
        arrs +=1
        a +=1

    for i in arr:
        sumatotal +=i

    minsum = abs(sumatotal - arr[arrs])
    maxsum = sumatotal - arr[0]

    print(minsum, maxsum)
