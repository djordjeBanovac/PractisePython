"""Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number. (If you don’t 
know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

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


def divisors(num:int)->None:
    """if divisor can divide num it will be added to the list"""
    divisor_list = []
    for divisor in range(1,int(num/2+1)):
        if num%divisor==0:
            divisor_list.append(divisor)
    divisor_list.append(num)
    print("divisor list:\n",divisor_list)


num = int(check_entry("Enter number:"))
divisors(num)
