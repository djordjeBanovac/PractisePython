"""Write a password generator in Python.
Be creative with how you generate passwords - strong passwords 
have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. The passwords should be random, generating 
a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import string
from random import SystemRandom

char_lowercase_digits = string.ascii_lowercase+string.digits
char_printable = string.printable

word_list = ['mum','dad','god','admin','strong','supermen','batmen','hologram','facebook', 'reload']
string_menu = "-------------------------------\n" \
              "------password generator-------\n" \
              "Options:\n" \
              "1.Weak password\n" \
              "2.Medium password\n" \
              "3.Strong password\n" \
              "4.Exit\n" \
              "Choose option(if left empty it will exit):"

def is_int(seq:str) ->bool:
    """Checks if number is entered"""
    try:
        int(seq)
        return  True
    except ValueError:
        return False


def correct_input(seq:str)->str:
    """promts user for correct input."""
    while True:
        user_input = input(seq)
        if is_int(user_input) or user_input=="":
            break
        else:
            print("Please enter a number, not something else.")
    return  user_input


def password_generator(choice:int, size=10) ->str:
    """function generates passwords. It can generate password from three lists and every list 
    is being used for one of the options. """
    osrand = SystemRandom()
    password = ''
    if choice == 1:
        print("Option one: weak password. Two words randomly chosen from the list.")
        password = ''.join([word_list[osrand.randint(1,len(word_list))],word_list[osrand.randint(1,len(word_list))]])
    elif choice == 2:
        print("Option two: randomly chosen numbers and lowercase letters.\n"
              "Password will have ",size," caracters. (default is 10)")
        password = ''.join([char_lowercase_digits[int(osrand.random()*len(char_lowercase_digits))] for elem in range(0, size)])
    elif choice == 3:
        print("Option three: randomly chosen from all printable caracters.\n"
              "Password will have ",size," caracters. (default is 10)")
        password = ''.join([char_printable[int(osrand.random()*len(char_printable))] for elem in range(0, size)])
    return password


def app() ->None:
    while True:
        user_in = int(correct_input(string_menu) or '4')
        if user_in == 1:
            passwd = password_generator(1)
            print( "Generated password: ", passwd )
        elif user_in == 2 or user_in==3:
            pass_len = int(correct_input("Enter password len (if empty it will be 10)") or '10')
            passwd = password_generator(user_in,pass_len)
            print("Generated password: ",passwd)
        elif 4:
            print("Exit")
            break
        else:
            print("No such option. Please enter again:")

if __name__ == '__main__':
    app()