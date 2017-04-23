"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below."""


from math import sqrt

def is_prime(num:int) -> bool:
    """checks if number is prime. It returns true if the number
    is prime or false if it is not. I for loop spins from 2 till sqrt(num)
    because it doesnt have to spin further than sqrt(num)."""
    prime = True
    for value in range(2,int(sqrt(num))):
        if num%value !=0:
            prime = False
            break
    return prime
