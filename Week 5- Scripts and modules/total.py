import sys
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