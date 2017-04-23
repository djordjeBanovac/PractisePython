"""Write a program that asks the user how many Fibonnaci 
numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to 
generate.(Hint: The Fibonnaci seqence is a sequence of numbers where 
the next number in the sequence is the sum of the previous two numbers 
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""


fibonnaci_iterative_list = [1,1]

def is_int(num:int) ->bool:
    try:
        int(num)
        return True
    except ValueError:
        return False

def correct_input(sequence:str) ->str:

    while True:
        num = input(sequence)
        if is_int(num):
            break
        else:
            print("You cannot enter letters where integer number is expected.")
    return num

def fibonnaci_iterative(num_range:int)->None:
    if num_range==1:
        fibonnaci_iterative_list.pop()
    else:
        for elem in range(1,num_range):
            fibonnaci_iterative_list.append(fibonnaci_iterative_list[elem]+fibonnaci_iterative_list[elem-1])

def fibonnaci_recursive(num_range:int) ->None:
    if num_range==0:
        return 0
    elif num_range==1:
        return 1
    else:
        return fibonnaci_recursive(num_range-1)+ fibonnaci_recursive(num_range-2)

fib_range = int(correct_input("Enter number of fibonnaci elements:"))
fibonnaci_iterative(fib_range)
print(fibonnaci_iterative_list)
fibonnaci_recursive_list = [fibonnaci_recursive(item) for item in range(0, fib_range)]
print(fibonnaci_recursive_list)