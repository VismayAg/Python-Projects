#!/bin/python3

import math
import os
import random
import re
import sys
from string import digits


#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
#---->MY CODE<------
def missingCharacters(s):
    a = [False for i in range(26)]
    for i in range(len(s)):
        if(s[i] >= 'a' and s[i] <= 'z'):
            a[ord(s[i]) - ord('a')] = True
    output = ''.join(c for c in digits if c not in s)
    for i in range(26):
        if(a[i] == False):
            output += chr(i+ord('a'))
    return output
#------>Ends<--------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
