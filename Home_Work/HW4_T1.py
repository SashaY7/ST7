#Write a script that will calculate the factorial of the entered number  without using recursion.

fact = int(input("Input number factorial: "))

import math

factorial = math.factorial(fact)

print (f'Factorial {fact} is {factorial} ')