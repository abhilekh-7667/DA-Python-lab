#program for assignment operator
n=int(input("Enter a number: "))
n+=3
print("After assignment:", n)
n-=2
print("After assignment:", n)
n *= 3 
print("After assignment:",n)
n = n / 4
print("After assignment:", n)

b=int(input("Enter another number:"))
b = b % 3
print("After assignment:", b)
b**= 3 
print("After assignment:", b)
b //= 2
print("After assignment:",b)