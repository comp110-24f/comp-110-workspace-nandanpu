"""This program utilizes the features of lists to create functions for lists."""
__author__ = "730768561"

def only_evens(arr : list[int]) -> list[int]: 
    even_arr : list[int] = [] 
    for item in arr: 
        if item % 2 == 0: 
            even_arr.append(item)
    return even_arr

def sub(arr : list[int], start : int, end : int) -> list[int]:     
    sub_arr : list[int] = [] 

    if len(arr) == 0 or start >= len(arr) or end <= 0: 
        return []

    if start < 0: # I forgot to take into account that the numbers in the range could be a negative number which could create the wrong output.
        start = 0
    if end > len(arr): 
        end = len(arr) 

    for index in range(start, end):
        sub_arr.append(arr[index])
    return sub_arr 

def add_at_index(arr : list[int], element : int, index : int) -> None: 
    if index < 0 or index > len(arr): 
        raise IndexError("Index is out of bounds for the input list")
    
    arr.append(element) 
    for item in range(len(arr) - 1, index, -1): 
        arr[item] = arr[item - 1]

    arr[index] = element

list_1 = [1, 2]
add_at_index(list_1, 3, 1)
print(list_1)