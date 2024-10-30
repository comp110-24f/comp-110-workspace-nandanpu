"""Sum the elements of a list"""
__author__ = "730761368"

def w_sum(arr : list[float]) -> float: 
    index : int = 0 
    sum : float = 0.0
    while index < len(arr): 
        sum += arr[index]
        index += 1
    return sum 

def f_sum(arr : list[float]) -> float: 
    sum : float = 0.0
    for item in arr: 
        sum += item
    return sum 

def f_range_sum(arr : list[float]) -> float: 
    sum : float = 0.0
    for index in range(0, len(arr)): 
        sum += arr[index] 
    return sum 

