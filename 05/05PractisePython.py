"""Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes."""

from random import randint

list_one = [randint(0,20) for elem in range(0,20)]
list_two = [randint(0,20) for elem in range(0,10)]

print('list 1:',list_one)
print('list 2: ',list_two)

def common_elements_list(list_one:list,list_two:list) -> list:
    """returns list with common elements"""
    common = []

    for elem in list_one:
       if elem in list_two and elem not in common:
           common.append(elem)
    return common

common_list = common_elements_list(list_one,list_two)
print("Common elements list: ", common_list)

