"""finds the max value in a list and removes"""
__author__ = "730761368"

def find_and_remove_max(arr : list[int]) -> int: 
    if len(arr) == 0: 
        return -1 
    
    max : int = arr[0] 
    for item in arr: 
        if max < item: 
            max = item 

    index : int = 0
    while index < len(arr): 
        if max == arr[index]: 
            arr.pop(index) 
        else:
            index += 1
    return max

