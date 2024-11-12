import functools
from functools import cache

def two_sum(lst,target):
    min = target
    res = ()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]+lst[j] == target and lst[i]<min:
                min = lst[i]
                res = (i,j)
    return res

def two_sum_hashed(lst,target):
    res = ()
    min = target
    for i in range(len(lst)):
        other = target - lst[i]
        if other in lst and i<min:
            min = i
            res = (i,lst.index(other))
    return res

def two_sum_hashed_all(lst,target):
    res = []
    for i in range(len(lst)):
        other = target - lst[i]
        if other in lst and (lst.index(other),i) not in res:
            res.append((i,lst.index(other)))
    return res

def memo(func):
    memo.cache = {}
    def memoized_func(*args):
        if args not in memo.cache:
            memo.cache[args] = func(*args)
        return memo.cache[args]
    return memoized_func

@memo
def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)

@cache
def fib_cached(n):
    if n<2:
        return 1
    return fib_cached(n-1)+fib_cached(n-2)

if __name__ == "__main__":
    print(two_sum([1,2,3,4,5,6,7,8],8))
    print(two_sum_hashed([1,2,3,4,5,6,7,8],8))
    print(two_sum_hashed_all([1,2,3,4,5,6,7,8],8))
    print(fib(10))
    print(fib(15))
    print(fib_cached(10))
    print(fib_cached(15))