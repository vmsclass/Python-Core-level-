# Program to detect even or odd using % operator
##number=int(input("Please enter a number\n"))
##
##if number%2==0:
##    print("The given number is even")
##else:
##    print("The given number is odd")
    
number=int(input("Please enter a number\n"))
result=int(number/2)*2
if number==result:
    print("The given number is even")
else:
    print("The given number is odd")
