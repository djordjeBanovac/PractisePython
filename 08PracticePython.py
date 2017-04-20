"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the 
players want to start a new game)"""


win = {'rock':'sissors',
       'sissors':'paper',
       'paper':'rock',}

command_list = ['rock','paper','sissors']

def is_int(num:int)-> bool:
    """checks if number is integer"""
    try:
        int(num)
        return True
    except ValueError:
        return False

def check_entry(entry:str) ->str:
    """function prompts for correct entry"""
    while True:
        num = input(entry)
        if is_int(num):
            break
        else:
            print("Not a number entered. Enter again.")
    return num

def user_input(name:str) -> str:
    """function prompts user for input, formats input properly. If command exists returns the command"""
    user_in = input(name+", choose your destiny:")
    user_in = user_in.lower()
    while True:
        if user_in in command_list:
            break
        else:
            print("No such command.Enter again.")
    return user_in

def game_logic(p1_name:str,p2_name:str) -> str:
    """Logic of the game. Cheks which of the players won based on the win dict."""
    p1_choise = user_input(p1_name)
    p2_choise = user_input(p2_name)

    if p1_choise == p2_choise:
        return 'tie'
    elif win[p1_choise] == p2_choise:
        return p1_name+' wins'
    else:
        return p2_name+' wins'


def game() ->None:
    """Function that runs the game."""
    while True:
        print("----ROCK-PAPER-SISSORS----")
        print("1.Game\n2.Exit\n")
        choise = int(check_entry("Choise:"))
        if choise == 1:
            name1 = input("Enter player 1 name:")
            name2 = input("enter player 2 name:")
            print(game_logic(name1,name2))
        elif choise == 2:
            print("exit game.")
            break
        else:
            print("No such choise")


game()