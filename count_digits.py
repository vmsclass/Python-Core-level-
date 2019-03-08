#  Description : program to print the total number of digits in a given positive
#  integer. For example if the number is 12345, the your output is 5.
#  Author : M. Sudhakar
#  Ex:  12345 ==> 1234 ==> 123 ==> 12 ==> 1 ==> 0
# Division (/) == quotient
# modulus (%) == remainder

n=int(input("enter a number"))
count=0
while n>0:
    n=n//10
    print("The n value",n)
    count=count+1
    print("The count value",count)
print("total number of digits",count)
    
