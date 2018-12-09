
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter # Counter class From Collection Module it return frequency of number in dict
# Complete the sockMerchant function below.
def sockMerchant(ar):
    c=Counter(ar)
    ls=list(c.values())
    i=0
    for x in ls:
        lm=x//2
        i+=lm
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
