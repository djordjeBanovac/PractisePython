"""Write a program (using functions!) that asks the user for a long 
string containing multiple words. Print back to the user 
the same string, except with the words in backwards order. For example, 
say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My"""


def reversed_string(sequence:str) ->str:
    """function splits string on white space and creates new string whit same words but in
    reverse order"""
    word_list = sequence.split(' ')
    return ' '.join(word_list[::-1])


string = input("Enter string:")
print("Reversed string: ",reversed_string(string))