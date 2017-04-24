"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old."""


def check_entry(entry:str)->int:
    """This function is safety. One cannot enter letters if number is expected"""
    while(True):
        num = input(entry)
        if isInt(num):
            break
        else:
            print("Please enter a integer!")
    return num

def isInt(age:int)->bool:
    """this function checks if age param is int. Returns true if yes. False if no"""
    try:
        int(age)
        return True
    except ValueError:
        return False

def repeat(num:int, sequence:str)->None:
    """Repeats sequence"""
    for i in range(num):
        print(sequence)

name = input("Name:")
enter_year = int(check_entry("Enter age:"))
repeat_num = int(check_entry("How many times to repeat:"))

result_string = name+" it will be year "+str(2017-enter_year+100)+" when you are 100 years old"
repeat(repeat_num,result_string)