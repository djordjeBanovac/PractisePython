"""Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last
elements of the given list. For practice, write this code inside a function."""

from random import randint

rand_list = [randint(0,50) for elem in range(0, randint(0,10))]

def first_and_last(param_list:list)->list:
    """function creates new list from the parameter list. pop() isn't used
    becuse it affects the original list."""
    if len(param_list)>1:
        result = [param_list[0],param_list[-1]]
    else:
        result = param_list
    return result

print("rand_list:\n",rand_list)
print("first and last list:\n",first_and_last(rand_list))
print("rand_list:\n",rand_list)
