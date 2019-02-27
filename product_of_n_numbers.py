#Description : Program to print the product of first 'n' natural numbers.
#                for example if n = 5, the output is 120.
#                           1 * 2 * 3 * 4 * 5 = 120
#product = 1
#product = 1 * 1 = 1
#product = 1 * 2 = 2
#product = 2 * 3 = 6
#product = 6 * 4 = 24
#product = 24 * 5 = 120
number = int(input("Enter a number"))
product = 1
##for i in range(1,number+1):
##    product = product * i

# while loop
i=1
while i<=number:
    product=product*i
    i=i+1
print("The product is : ",product)

# factorial of a given number n! = n * (n-1) * (n-2) *.... 1
# 5 ! = 5 * 4 *3 *2 *1 = 1*2*3*4*5 


