"""This file helps visualize and utilize the contents of concatentation and coordinates."""
__author__ = "730768561"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x : str = "123" 
y : str = "abc" 

print(concat(str1 = x, str2 = y))
get_coords(xs = x, ys = y) # At first, I tried to print this statement without realized the functions has a Nonetype return type. 