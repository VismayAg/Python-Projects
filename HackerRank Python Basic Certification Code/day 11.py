#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    n = 6
    m = []
    for i in range(n):
        m.append(list(map(int, input().split()[:n])))

    def sum_glass(m, i, j):
        return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])

    best = float("-inf")
    for i in range(4):
        for j in range(4):
            s = sum_glass(m, i, j)
            if s > best:
                best = s

    print(best)
