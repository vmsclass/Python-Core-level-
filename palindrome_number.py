# Description : program to check the given number is palindrome or not.
# Ex: n = 123, rev = 321 ; not a palindrome
# Ex: n = 121, rev = 121 ; palindrome
# Step 1: read a number (n = 121)
# Step 2: reverse the number (rev = 121)
           # last_digit = n%10
           # rev= rev* 10 + last_digit
           # n = n/10
# Step 3: if n == rev ; then palindrome; otherwise not a palindrome.

n=int(input("enter a number"))
temp=n
rev=0

while n>0:
    last_digit=n%10
    rev=rev*10 + last_digit
    n=n//10
print("the reversed number is ",rev)

if temp==rev:
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")


