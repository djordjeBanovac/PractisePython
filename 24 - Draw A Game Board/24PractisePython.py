"""This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. 
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game 
boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come 
in many other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw 
it for them to the screen using Python’s print statement.
Remember that in Python 3, printing to the screen is accomplished by
print("Thing to show on screen")"""


def draw_grid(width: int, height: int) -> None:
    """this function utilizes two for loops and the fact that
    there are 15 symbols in a row. it allows you to have a 3x4, 4x5, 5x6 etc grid."""
    for i in range(height*2+1):
        for j in range(width*5+1):
            if i % 2 == 0:
                if j % 5 == 0:
                    print(" ", end="")
                else:
                    print("-", end="")
            else:
                if j % 5 == 0:
                    print("|", end="")
                else:
                    print(" ", end="")
        print()


def draw_grid2(height: int, width: int) ->None:
    """The grid consists out of repeating sequences
    ' ---' and '|   '. It allows inconsistent grid dimensions: 3x4,3x6,4x7 etc.
    This function is more efficient and more optimal than the last one."""
    for i in range(height+1):
        print(" ---" * width)
        if i < height:
            print("|   " * width, "|", sep="")


def user_entry(sequence: str) ->int:
    """Prompts user for entry"""
    while True:
        try:
            entry = int(input(sequence))
            return entry
        except ValueError:
            print("Please enter integer number, not something else.")


if __name__ == "__main__":
    print("---------------------------\n"
          "--------Grid drawer--------\n")
    height = user_entry("Enter grid height:")
    width = user_entry("Enter grid width:")
    draw_grid2(height, width)