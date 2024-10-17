"""Mutating functions."""
__author__ = "730768561"

def manual_append(array : list[int], number : int) -> None: # I had to get used to using the list[int] as the type for array parameters.
    array.append(number)

def double(array : list[int]) -> None:
    index : int = 0
    while index < len(array):
        array[index] *= 2 
        index += 1

list_1 : list[int] = [1, 2, 3]
list_2 : list[int] = list_1 

double(list_2) 
print(list_1) 
print(list_2) 