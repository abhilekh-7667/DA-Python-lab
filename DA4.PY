# taking 3 numbers as input and printing the largest
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
o = int(input("Enter third number: "))

if m>n and m>o:
    print("GREATEST number is",m)
elif n>o:
    print("GREATEST number is:", n)
else:
    print("GREATEST number is:", o)