"""Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)"""


def isPalindrome(seq:str)->str:
    """function checks if the string seq is palindrome or not"""
    if seq==seq[::-1]:
        result = seq + " is palindrome"
    else:
        result = seq + " isn't palindrome"
    return result

print(isPalindrome(input("Enter string to check whether the string is palindrome or not:")))


