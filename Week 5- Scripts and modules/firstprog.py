#This program will first ask for  a number to be input.
number = input("Enter a number: ")
#This is used to let the program know that the number is an integer so the control statements work on it.
number = int(number)
#This will tell the user what number they have entered.
print("The number entered was", number)
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")
#This if an else control statement will make it so they check if the number is even or odd and will then tell the user which one they are.

if (number % 10) == 0:
    print("This number is divisible by 10.")
else:
    print("This number is not divisble by 10.")