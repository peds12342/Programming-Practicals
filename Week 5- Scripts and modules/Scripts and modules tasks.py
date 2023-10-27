import sys
number = input("Enter a number: ")
number = int(number)
print("The number entered was", number)
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")
if (number % 10) == 0:
    print("This number is divisible by 10.")
else:
    print("This number is not divisible by 10.")


count = len(sys.argv)
if count <= 1:  #If no arguments provided will print this message.
    print("No arguments were provided.")
else:
    total = 0
    for i in range(1, count):
        total += float(sys.argv[i])  #This will take all the values and total them.

    average = total / (count - 1)  #This will take the total and use it to work out the average.
    print("Total is", total)
    print("Average is", average)
#This program will take the command line arguments provided and calculate the total then\
#the average of the arguments provided, if no arguments provided it will give the user a message.


def average(values):
    """Calculates the average of the given list."""
    total = 0
    for n in values:
        total += float(n)
    return total / len(values)

# Initialization statement
print("Welcome, utils module has been imported and initialized!")

import utils.py
print("Average is", utils.average([10, 23, 30]))
print("Another average is", utils.average([10.2, 8.8, 2.6]))


from utils import average

print("Average is", average([10, 23, 30]))
print("Another average is", average([10.2, 8.8, 2.6]))


import math
print(dir(math))


print("The import search path for this program is", sys.path)
