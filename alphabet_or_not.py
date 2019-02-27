#Description : Python program to check the given character is alphabet or not
# Alphabets : a-z or A-Z
# Author : M. Sudhakar
ch= input("Please enter any character:")

if (ch >= 'a' and ch<='z') or (ch>= 'A' and ch <='Z'):
    print(ch,"is an alphabet")
else:
    print(ch,"is not an alphabet")
