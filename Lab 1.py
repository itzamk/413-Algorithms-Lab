'''
Andrew Kozempel
CMPSC 413
Lab 1
Fall 2023
'''

import math
import random
import time

############################################################
#  PART 1 - GCD
############################################################

# best case: O(1)
# worst case: O(n), n = min(num1,num2)
def GCD(num1, num2):

    start = time.time_ns()

    # test numbers ranging from the smaller number to 1
    for i in range(min(num1,num2), 0, -1):

        # if both numbers are divisible by i, return i
        if num1 % i == 0 and num2 % i == 0:
            return i, time.time_ns() - start

# Test cases
gcd_test_cases = [(100, 25), 
                  (48, 18), 
                  (17, 5),
                  (12345, 67890),
                  (234567, 765432)]

# print result and expected to verify
print("\n\tPART 1: GCD")
for a, b in gcd_test_cases:

    gcd, gcd_time = GCD(a,b)

    print(f"\nTesting: {a}, {b} \
          \nResult: {gcd} \
          \nExpected: {math.gcd(a,b)} \
          \nTime: {gcd_time} nanoseconds")


############################################################
#  PART 2 - Min/Max
############################################################

def min_max(list):

    start = time.time_ns()

    # initialize min,max as first element for future comparisons
    min = list[0]
    max = list[0]

    # iterate through all elements in the list
    for i in list:

        # if i is larger than max, assign it as max
        if i > max:
            max = i

        # if i is smaller than min, assign it as min
        elif i < min:
            min = i

    return min, max, time.time_ns() - start

def find_max(list):

    start = time.time_ns()

    # initialize min,max as first element for future comparisons
    max = list[0]

    # iterate through all elements in the list
    for i in list:

        # if i is larger than max, assign it as max
        if i > max:
            max = i

    return max, time.time_ns() - start

def find_min(list):

    start = time.time_ns()

    # initialize min,max as first element for future comparisons
    min = list[0]

    # iterate through all elements in the list
    for i in list:

        # if i is larger than max, assign it as max
        if i < min:
            min = i

    return min, time.time_ns() - start

# test cases
minmax_test_cases = [[],[]]

for i in range(1000):
    minmax_test_cases[0].append(random.randint(1,100000))

for i in range(10000):
    minmax_test_cases[1].append(random.randint(1,100000))

# print min and max values
print("\n\tPART 2: MIN AND MAX")
for test in minmax_test_cases:
    #min_val, max_val, mm_time = min_max(test)
    min_val, min_time = find_min(test)
    max_val, max_time = find_max(test)
    print(f"\nTesting: {len(test)} elements \
          \nResult:   Min: {min_val}, Max: {max_val} \
          \nExpected: Min: {min(test)}, Max: {max(test)} \
          \nMin Time: {min_time} nanoseconds\
          \nMax Time: {max_time} nanoseconds")
    
############################################################
#  PART 3 - Min/Max
############################################################