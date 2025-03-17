#Python program to find all possible pairs with given sum
  #Replace the `lst` variable with any column of your dataframe (df.column ou df['column'])

# IMPORT LIBRARIES
import numpy as np  # linear algebra
import pandas as pd # data processing
import itertools    # loop

# FIND PAIRS
# Python3 program to find all pairs in
# a list of integers with given sum

def findPairs(lst, K):
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))

    res.reverse()
    return res

# Driver code
lst = [1812.91, 13.81, 30, 39.65, 75.6, 568, 24.94, 180, 2175.77, 625.92, 7872.42, -15.3, -2.16, -46.54, -13.76,2172.18, 1568.49, 449.06, 2087.83, 2413.19, 386.8, 656.34, 105.5, 2480.28, 618.66, 288.16, -70.96, -512.41, -158, -2.38, 2889.65, 173.3, 2660, 143.91, 46.72, 1688.48, 3114.52, 117.56, 3131.72, 353.36, -85.26, -726.63, -3.21, -1868.74, -21.75, -125.52, -1005.53, -1705.96, -912.31, -1204.88,29979.1, 308.67, 231.45, 16.13, 2426.9, 611.25, 994.74, -150, -570.48, -67.2, -435.57, -594.78, -485.66, -1663.99,4786.54, 445.67, 591.25, 1315.15, 2555.92, 307.17, 1649.79, 2735.15, -1881.59, -8885.05, -2047.15, -525.07, -466.73, -1858.98, -1744.55, -3209.3, -185.16, -416.94, -355.96,1227.74, 2671.17, 2538.88, 330.91, 3684.1, 395.71, 495.36, 1900.07, 280.08, 3019.73, 3915.54, 548.4, 180, 346.25, 31057.62, 1117.08, 341.69, -1269.98, -1776.7, -708.33, -590.19, -237.27, -197.11, -370.9, -91.8, -81.6, -1908.01, -4.8, -1512.92, -272.8, -9993.05, -1881.62,2108.06, 3358.19, 265.11, 457.34, 1510.86, 2386.97, 732.83, 276.92, 2326.24, 3307.77, 217.01, 1285.46, 2364.93, 436.44, -1019.91, -1539.78, -1295.99, -189.83, 0, -1834.91, -675, -81.6, -2069.01, -913.66, -999.74, -5203.15, -1674.56]   #FACTURES
K = 4416.93            #PAIEMENT
print(findPairs(lst, K))

# FIND COMBINATIONS
import itertools

def find_combinations(lst, K):
    def find_combos(lst, target, partial=[]):
        s = sum(partial)

        # check if the partial sum is equals to target
        if s == target:
            result.append(partial)
        if s >= target:
            return  # if we reach the number why bother to continue

        for i in range(len(lst)):
            n = lst[i]
            remaining = lst[i+1:]
            find_combos(remaining, target, partial + [n])

    result = []
    find_combos(lst, K)
    return result

# Driver code
lst = [449.06, 386.8, 105.5,29979.1, 16.13, 994.74,445.67, 1315.15, 1649.79,1227.74, 2538.88, 3684.1, 495.36, 1900.07, 280.08, 3019.73, 548.4, 180, 31057.62, 1117.08, 341.69 ]   #FACTURES
K =  2803.99               #PAIEMENT
result = find_combinations(lst, K)
print(result)
