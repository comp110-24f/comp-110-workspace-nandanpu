"""Finds the max value in a list and removes all occurences"""
__author__ = "730768561"

def find_and_remove_max(arr : list[int]) -> int: 
    if len(arr) == 0: 
        return -1 
    
    max : int = arr[0] 
    for item in arr: 
        if max < item: # I accidentally put max > item rather than max < item which led to an incorrect output. 
            max = item 

    i : int = 0
    while i < len(arr): 
        if max == arr[i]: # For this while loop, I had to take into account edge cases such as if two values are next to each other I needed to make sure that the index value isn't increased or it would create the wrong output.
            arr.pop(i) 
        else:
            i += 1
    return max

