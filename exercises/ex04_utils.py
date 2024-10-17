"""This program utilizes the properties of arrays to mutate and check the contents of arrays."""
__author__ = "730768561"

def all(arr : list[int], number : int) -> bool: 
    if len(arr) == 0: # I forgot to check for empty lists. 
        return False
    for item in arr: 
        if (item != number): 
            return False
    return True

def max(arr : list[int]) -> int: 
    if len(arr) == 0: 
        raise ValueError("max() arg is an empty List")
    maxVal : int = -999 # I needed to make sure that this value is set to the smallest number so that max value could work correctly.
    for item in arr: 
        if item > maxVal: 
            maxVal = item
    return maxVal

def is_equal(arr1 : list[int], arr2 : list[int]) -> bool: 
    if len(arr1) != len(arr2): # I needed to make sure that the two list objects are the same length before moving onto other conditionals.
        return False
    else: 
        for i in range(0, len(arr1)): 
            if arr1[i] != arr2[i]: 
                return False
        return True

def extend(arr1 : list[int], arr2 : list[int]) -> None: # At first, I thought that it would return a list, so I tried to use the list type as the return value, but I soon realized I'm just supposed to mutate a list rather than returning a whole new list object.
    for item in arr2: 
        arr1.append(item) 

