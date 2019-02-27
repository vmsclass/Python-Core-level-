#Description: Python Program to check the given character is vowel or not.
#Vowels : a,e,i,o,u (A,E,I,O,U)
#Author : M. Sudhakar
ch=input("please enter a character")
#Method1
##if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or
##    ch== 'A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
##    print(ch,"is a vowel")
##else:
##    print(ch,"is not a vowel")

#Method2
vowels=['a','e','i','o','u','A','E','O','I','U']

if ch in vowels:
    print(ch,"is a vowel")
else:
    print(ch,"is not a vowel")
