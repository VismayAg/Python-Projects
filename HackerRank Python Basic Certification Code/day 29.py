#!/bin/python3

import math
import os
import random
import re
import sys

def max_bit(n,k):
    maximum = 0
    for i in range(1,n+1):
        for j in range(1,i):
            h = i & j
            if maximum < h < k:
                maximum = h
            if maximum == k-1:
                return maximum
    return maximum

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        print(max_bit(n,k))