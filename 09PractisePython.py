"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""


from random import randint



def is_int(num:int)->bool:
    """cheks if number is int"""
    try:
        int(num)
        return True
    except ValueError:
        return False


def check_entry(message:str)->str:
    """checks if entry is correct"""
    while True:
        entry = input(message).lower()
        if is_int(entry) or entry=='exit':
            break
        else:
            print("You entered ",entry,". Please, you have to enter integer number.")
    return entry

def game() ->None:
    """function that runs the game. It stops when num is guessed or exit is typed"""
    num_guesses = 0
    rand_num = randint(0, 9)
    while True:
        guess = check_entry("Enter number or exit:")
        if guess == 'exit':
            break
        else:
            if int(guess) == rand_num:
                print( "You guessed correctly! It took you only ", num_guesses, "to guess the number!" )
                num_guesses = 0
                rand_num = randint(0,9)
            else:
                if int( guess ) > rand_num:
                    print( "Guess is too high." )
                else:
                    print( "Guess is too low." )
                num_guesses += 1
    if guess == 'exit' and num_guesses==0:
        print("Exit game")
    elif guess=='exit' and num_guesses>0:
        print("Exit game. It took you ", num_guesses," but you didn't guessed the number.")

game()