from typing import List


def partition(index: int , X:List[int]) -> None:
    pivot = X[index]
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            if X[j] < pivot:
                X[i],X[j] = X[j],X[i]
                break
    for i in reversed(range(len(X))):
        for j in reversed(range(i)):
            if X[i]>pivot:
                X[i],X[j]=X[j],X[i]
    return X

print(partition(0,[0,1,2,0,2,1,1]))