"""Write a program (function!) that takes a list and returns 
a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""


from random import randint

rand_list = [randint(0,50) for item in range(0,20)]
rand_list_two = [randint(0,50) for elem in range(0,25)]

def no_duplicates_list(param_list:list) ->list:
    """returns list with no duplicate elements"""
    ret_list = []
    for elem in param_list:
        if elem not in ret_list:
            ret_list.append(elem)
    return ret_list


def no_duplicates_list_set(param_list:list) ->list:
    """returns list with no duplicate elements using sets"""
    return list(set(param_list))


def common_elements(param_list1:list, param_list2:list) ->list:
    """returns list that contains common elements in two lists using sets"""
    return list(set(param_list1).intersection(set(param_list2)))

print("Rand_list:\n",rand_list)
print("\nRand_list2:\n",rand_list_two)
print("\nNo duplicates list:\n",no_duplicates_list(rand_list))
print("\nno duplicates list set:\n",no_duplicates_list_set(rand_list))
print("\nCommon elements:\n",common_elements(rand_list,rand_list_two))
