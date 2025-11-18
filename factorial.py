number=int(input("Enter a number:"))
fact=1
if number > 0:
    for i in range(1,number+1):
        fact=fact*i
print("Factorial",fact)