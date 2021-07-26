import math

## To calculate parity of the given integer. Parity:0 if number of 1's in bits is even, else 0.

# Brute force - bitwise check

def parity_calculator(x:int) -> int:
    score=0
    while x:
        score ^= x & 1
        x >>=1
    return score

print(parity_calculator(2^64))
# complexity O(n), n is word size 

# Approach 2: Drop lowest set bit 

def parity_calculator2(x:int) -> int:
    score =0 
    while x:
        score ^= 1
        x &= x-1 # droping the lowest set bit result : x&(x-1)
    return score 

print(parity_calculator2(2^64))
# time complexity O(k), k is the number of bit sets to 1 
