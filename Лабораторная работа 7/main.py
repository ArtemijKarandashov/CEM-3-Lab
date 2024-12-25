from functools import cache 

@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def two_sum(lst,target):
    min = target
    res = ()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]+lst[j] == target and lst[i]<min:
                min = lst[i]
                res = (i,j)
    return res