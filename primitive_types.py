import math


def parity_calculator(x:int) -> int:
    score=0
    while x:
        score ^= x & 1
        x >>=1
    return score

print(parity_calculator(2^64))
