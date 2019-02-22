number=int(input("Enter a number:"))
count=0

for i in range(1,number+1):
    if number%i != 0:
        print(i)
        count=count+1

print("The total number of factors :",count)
