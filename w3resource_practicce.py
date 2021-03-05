# a = input("Enter your first name: ")
# b = input("Enter your last name: ")
# c = (a  + ' ' +  b)


# x=[a]
# y=[b]
# z=c.reverse()

# print(z)

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[-1],color_list[-2])


# userinput=int(input("enter any number between 1 to 5: "))
# for i in range(1,userinput):
#     factorial=userinput*(userinput-1)
    
# print(factorial)



import random
ans=(random.randint(1,9))

for i in range(5):
    
    
    i = int(input("Enter any number between 1 to 9: "))
    if i == ans:
        print("correct")
        break
    elif i >= ans:
        print("your number is high")
    elif i <= ans:
        print("number is low")
    else:
        print("try again")
    
        



     