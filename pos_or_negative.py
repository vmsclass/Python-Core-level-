# Description: A program to check the given number is positive or negative
# Author : M. Sudhakar

number=int(input("Enter a number"))

##if number > 0:
##    print("The given number is positive")
##elif number < 0:
##    print("The given number is negative")
##else:
##    print("The given number is 0")
    
if number>=0:
    if number == 0:
        print("The given number is 0")
    else:
        print("The given number is positive")
else:
    print("The given number is negative")
