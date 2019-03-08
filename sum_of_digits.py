# Description : Program to print the sum of individual digits in a given number.
# Example : 462 , then your output is 12. (4+6+2)
# 462 ===> 4 + 6 + 2  ( Human : left to right)
# 462 ===> 2 + 6 + 4  ( Program logic : right to left)
# sum = 0
# n = 462   (n > 0)
# Step 1: find the last_digit (last_digit = n%10)
# Step 2: add the last_digit with the sum (sum = sum + last_digit)
# Step 3: remove the last_digit  ( n = n//10 )
# repeat step 1 to 3 until the n>0 false.
# sum = 0
# sum = 0 + 2 = 2
# sum = 2 + 6 = 8
# sum = 8 + 4 = 12
n=int(input("enter a number"))
sum=0
while n>0:
    last_digit=n%10
    sum=sum+last_digit
    n=n//10
print("The sum of individual digits",sum)
