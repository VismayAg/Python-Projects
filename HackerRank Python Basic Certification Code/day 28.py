#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    nw = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if '@gmail.com' in emailID:
            nw.append(firstName)
    
    nw = sorted(nw)
    for item in nw:
        print(item)
