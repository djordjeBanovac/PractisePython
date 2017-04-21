"""Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

def is_int(num:int)->bool:
    """validation if num is int"""
    try:
        int(num)
        return True
    except ValueError as err:
        return False



def check_entry(entry:str)->int:
    """Checks if letter is entered insted of number"""
    while True:
        num = input(entry)
        if is_int(num):
            break
        else:
            print("Please enter integer!")
    return num

def even_odd(num)->None:
    """function checks if the num is even, odd or multiple of four"""
    if num % 4 == 0:
        print("Entered number is multiple of four")
    else:
        if num%2==0:
            print("Entered number is even")
        else:
            print("Entered number is odd")


def run_even_odd()->None:
    """runs even_odd func"""
    print("--------------------------------------------------------")
    print("----------------------even and odd----------------------")
    num = even_odd(int(check_entry("Enter number:")))


def run_check_and_num() -> None:
    """runs bonus question"""
    print("---------------------------------------------------------")
    print("----------------------check and num----------------------")
    num = int(check_entry("Enter num:"))
    check = int(check_entry("Enter check:"))

    if num%check == 0:
        print(check," divides evenly into ",num)
    else:
        print(check, "doesn't divide evenly into ",num)


run_even_odd()
run_check_and_num()