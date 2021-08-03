from typing import List



# Two pass approach
def partition(index: int , X:List[int]) -> None:
    pivot = X[index]
    # Pass 1
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            if X[j] < pivot:
                X[i],X[j] = X[j],X[i]
                break
    #Pass 2
    for i in reversed(range(len(X))):
        for j in reversed(range(i)):
            if X[i]>pivot:
                X[i],X[j]=X[j],X[i]
    return X

# print(partition(2,[0,1,2,0,2,1,1]))
# result : [1, 0, 0, 1, 1, 2, 2]


def partition2(pivot_index:int,X:List[int])-> None:
    pivot = X[pivot_index]
    smaller=0
    for i in range(len(X)):
        if X[i] < pivot_index:
            X[i],X[smaller] = X[smaller],X[i]
            smaller +=1

    larger = len(X) -1
    for i in reversed(range(len(X))):
        if X[i] > pivot_index:
            X[i],X[larger] = X[larger],X[i]
            larger -= 1

    return X

# print(partition2(1,[0,1,2,0,2,1,1]))
# # result : [0, 0, 1, 1, 1, 2, 2]


#Single Pass approach
def partition3(pivot_index:int,X:List[int])->None:
    pivot = X[pivot_index]
    smaller,mid,larger = 0,0,len(X)

    while mid < larger:
        if X[mid] < pivot:
            X[smaller],X[mid] = X[mid],X[smaller]
            smaller,mid = smaller+1,mid+1
        elif X[mid] == pivot:
            mid+=1
        else:
            larger -= 1
            X[mid],X[larger]=X[larger],X[mid]

    return X

# print(partition3(1,[0,1,2,0,2,1,1]))
# # result : [0, 0, 1, 1, 1, 2, 2]





    

