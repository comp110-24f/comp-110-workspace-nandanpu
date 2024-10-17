"""Testing file for the find_max function"""
__author__ = "730768561"
from CQs.cq07.find_max import find_and_remove_max

def test_find_and_remove_max() -> None:
    assert(find_and_remove_max([9,4,3,2,10]) == 10)

def test_mutate_find_and_remove_max() -> None: 
    b : list[int] = [9,4,3,2,10]
    find_and_remove_max(b) 
    assert(b == [9,4,3,2])

def test_edge_find_and_remove_max() -> None: 
    assert(find_and_remove_max([]) == -1)

