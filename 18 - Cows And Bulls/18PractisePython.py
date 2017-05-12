"""Create a program that will play the “cows and bulls” game with the user. 
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout the
 game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number."""

from random import randint


def user_entry(sequence: str)-> int:
    """used for correct user entry. Only the numbers are allowed"""
    while True:
        try:
            entry = int(input(sequence))
            return entry
        except:
            print("Please enter integer number, not something else")


def parse_num(num:int) ->list:
    """Function is used to parse umber into digits.
    Digits are stored in list and the list is returned"""
    digit_list = []
    while num!=0:
        digit_list.insert(0,num%10)
        num = int(num/10)
    return digit_list


def check_num(parsed_rand_num:list, user_num:int)->dict:
    """function checks if digits in user_num and digits in randomly
    generated number are equal. It returns dictionary."""
    cows_bulls = {'cows':0,'bulls':0}
    parsed_user_num = parse_num(user_num)

    for i in range(len(parsed_user_num)):
        if parsed_user_num[i] in parsed_rand_num:
            if parsed_user_num[i] == parsed_rand_num[i]:
                cows_bulls['cows']+=1
            else:
                cows_bulls['bulls']+=1
    return cows_bulls


def game() ->None:
    """Game launcher"""
    print("Cows and bulls game")
    rand_num = randint(1000,9999)
    print(rand_num)
    rand_num_digits = parse_num(rand_num)

    while True:
        user_num = user_entry( "Get me a number:" )
        cows_bulls = check_num(rand_num_digits,user_num)

        if cows_bulls['cows'] == 4:
            print( "You won! The number was: ", rand_num )
            break
        else:
            print(cows_bulls['cows']," cows, ", cows_bulls['bulls']," bulls")


if __name__ =="__main__":
    game()