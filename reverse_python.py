#Description: Program to print the reverse number of a given number.
#Author : M. Sudhakar

n=int(input("enter a number"))

rev=0

while n>0:
    last_digit = n%10
    rev=rev*10 + last_digit
    n=n//10

print("The reversed number is ",rev)
    
    
    
    
    
