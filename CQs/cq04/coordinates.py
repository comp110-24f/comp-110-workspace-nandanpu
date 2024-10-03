"""This file gets the coordinates from a string of text."""
__author__ = "730768561"

def get_coords(xs : str, ys : str) -> None: 
    i : int = 0 
    while i < len(xs): 
        j : int = 0 
        while j < len(ys): 
            print(f"{xs[i],ys[j]}")
            j += 1 # I forgot to add the indexes by 1 every iteration, so it just led to an infinite loop after running this file. 
        i += 1
        