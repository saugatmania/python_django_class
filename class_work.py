def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b 

def division(a,b):
    return a / b 

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(" 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division")

choice= int(input("Enter your choice"))

if choice == 1:
    print("addition is", addition(num1,num2))
elif choice == 2:
    print("subtraction is", subtraction(num1,num2))
elif choice == 3:
    print("multiplication is", multiplication(num1,num2))
elif choice == 4:
    print("division is", division(num1,num2))
else:
    print("ERROR")