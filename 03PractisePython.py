"""Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, 
make a new list that has all the elements less than 5 from this 
list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the user."""


import random

rand_list = [random.randint(0,100) for i in range(0,20)]


def less_then_five(array_list:list)->None:
    """prints all elements of the list less than five"""
    # for elem in array_list:
    #     if elem<5:
    #         print(elem)
    new_list = [elem for elem in array_list if elem < 5]
    print(new_list)


def check_entry(entry:str)->int:
    """This function is safety. One cannot enter letters if number is expected"""
    while(True):
        num = input(entry)
        if isInt(num):
            break
        else:
            print("Please enter a integer!")
    return num

def isInt(num:int)->bool:
    """this function checks if age param is int. Returns true if yes. False if no"""
    try:
        int(num)
        return True
    except ValueError:
        return False

def smaller_than_entered_number(array_list:list, num:int) -> None:
   """returns list from original list that are smaller than num"""
   new_list = [elem for elem in array_list if elem < num]
   print(new_list)



#test
print("\nrand_list:",rand_list)
print("\n------------Print elements smaller than five-----------------")
print("-------------------------------------------------------------")
less_then_five(rand_list)
print("----------Print elements smaller than entered number---------")
print("-------------------------------------------------------------")
num = int(check_entry("Enter number:"))
smaller_than_entered_number(rand_list,num)