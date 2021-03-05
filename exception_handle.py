# take two user input, convert into int
# print their sum


try:    
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    ans = num1 + num2
    # print(ans)
    
except ValueError as err:
    print("alphabet char can not be converted to int")
except NameError as err:
    print(err)
else:
    print(ans)
finally:
    print("Close programme")

name = input("Enter your name: ")
contact = input("Enter your contact number: ")
print(f"Your name is {name}")
print(f"Your contact is {contact}")

# try:
#     pass
# except Exception
#     pass
# except Exception
#     pass
# except Exception
#     pass
# else:
#     pass
# finally:
#     pass