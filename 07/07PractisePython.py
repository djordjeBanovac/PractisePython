"""Let’s say I give you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list 
that has only the even elements of this list in it."""

import random

rand_list = [random.randint(0,50) for elem in range(0,15)]
print("rand_list:\n",rand_list)

even_list = [elem for elem in rand_list if elem%2==0]
print("even elements from rand_list:\n", even_list)