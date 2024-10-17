"""Summing the elements of a list using different loops"""
__author__ = "730768561"

def w_sum(vals : list[float]) -> float: 
    i : int = 0 
    sum : float = 0.0
    while i < len(vals): 
        sum += vals[i]
        i += 1
    return sum 

def f_sum(vals : list[float]) -> float: 
    sum : float = 0.0
    for item in vals: 
        sum += item
    return sum 

def f_range_sum(vals : list[float]) -> float: 
    sum : float = 0.0
    for i in range(0, len(vals)): #At first, I didn't know if the second arguement for range was inclusive or exclusive, so I tried different arguments and realized that the second arguement is exclusive.
        sum += vals[i] 
    return sum 
