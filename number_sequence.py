#Description : A Program to print numbers in sequence
# 1. print numbers from 1,2,3,4,.....10
# 2. print numbers from 1,2,3,4,.....n
# 3. print numbers from 1,3,5,7......n (odd numbers)
# 4. print numbers from 2,4,6,8......n (even numbers)
# 5. print numbers from 50 to 100 (even numbers)
# Author : M. Sudhakar 

n=int(input("please enter a number"))
##for i in range(50,101,2):
##    print(i)


for i in range(n+1):
    if i%2!=0:
        print(i)
