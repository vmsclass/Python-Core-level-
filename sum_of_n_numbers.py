# Description : Program to print the sum of first 'n' numbers. for ex: n=10
#                1+2+3+4+5+6+7+8+9+10 = 55

# Initialize sum = 0
# Loop
# sum = 0  + 1 = 1
# sum = 1  + 2 = 3
# sum = 3  + 3 = 6
# sum = 6  + 4 = 10
# sum = 10 + 5 = 15
# sum = 15 + 6 = 21
# sum = 21 + 7 = 28
# sum = 28 + 8 = 36
# sum = 36 + 9 = 45
# sum = 45 + 10 = 55
# for loop
##n=int(input("enter a number"))
##sum=0
##for i in range(1,n+1):
##    sum=sum+i
##print("The sum is : ",sum)

# while loop
n=int(input("enter a number"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum is: ",sum)
    






