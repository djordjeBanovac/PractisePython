"""Write a function that takes an ordered list of 
numbers (a list where the elements are in order from 
smallest to largest) and another number. The function 
decides whether or not the given number is inside the 
list and returns (then prints) an appropriate boolean.

Extras:

Use binary search."""

from random import randint


def search(ordered_list:list, num:int) ->bool:
    """search with the keyword 'in'"""
    if num in ordered_list:
        return True
    else:
        return False

def bin_search(ordered_list:list, num:int) ->bool:
    """Binary search. One of the versions"""
    if num is ordered_list[0] or num is ordered_list[-1]:
        return True
    else:
        start = 1
        end  = len(ordered_list)-1

        while True:
            middle_index = int( (end - start)/2 )

            if middle_index<start or middle_index>end or middle_index<0:
                return False

            middle_elem = ordered_list[middle_index]

            if middle_elem is num:
                return True
            elif middle_elem>num:
                end = middle_index
            elif middle_elem < num:
                start = middle_index




if __name__ == "__main__":
    ordered_list = [4,7,11,14,16,17,22,44,65,76,81,82,90]
    num = randint(0,90)
    print(num)
    print(ordered_list)
    print(search(ordered_list,num))
    print(bin_search(ordered_list,num))
