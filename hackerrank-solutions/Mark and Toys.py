#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    numOfToys = 0
    spendMoney = 0
    prices.sort()
    for price in prices:
        if price + spendMoney <= k:
            spendMoney += price
            numOfToys += 1
            
    return numOfToys

def insetToPriceArray(pArray, num):
    size = len(pArray)
    for p in range((size - 1), 0, -1):
        if pArray[p] >= pArray[p-1]:
          return pArray[p]
        pArray[p], pArray[p-1] = pArray[p-1], pArray[p]  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
