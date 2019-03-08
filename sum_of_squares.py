# Description : Program to print the sum of squares of first 'n' natural numbers
# Input : number
# Output : sum of squares up to the number.
# Author : M. Sudhakar
sum=0
number=int(input("enter a number"))

##for i in range(1,number+1):
##    sum=sum+(i*i)

#while loop
i=1
while i<=number:
    sum=sum+(i*i)
    i=i+1
print("The total sum is ",sum)
