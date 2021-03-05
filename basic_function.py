# def hello():
#     print("welcome function")

# hello()

# def hello(name): #parameter
#     print("welcome",name)

# def bye(name): #parameter
#     print("bye",name)

# name=("enter your name: ")
# hello("Ram") #argument
# bye("shyam") #argument
# hello("saugat")



# def even_odd(num):
    
#     if(num%2==0):
#         print("You have entered even number.")
#     else:
#         print("You have entered odd number.")   

# even_odd(int(input("Enter a number: ")))



# def positive_negative(num):

#     if(num>0):
#         print("You have entered positive number.")
#     elif(num<0):
#         print("You have entered negative number.")
#     elif(num==0):
#         print("This number is neither negative nore positive.")

# positive_negative(int(input("Enter a number: ")))

    


# def display_profile(name, address, contact, country="China"): #parameter, #default argument
#     print("Name:", name)
#     print("address:", address)
#     print("contact:", contact)
#     print("country:", country)

# display_profile("Ram", "KTM" , "989898", "Nepal") #positional argument

# print("------------------------------------------------------")

# display_profile(name="Hari", contact="989898", address="PKR",) #Keyword argument

def hello(a,b):
    print("welcome",a,"how are you mr.",a)
    print("is your last name ",b)
    

hello(input("enter a name: "),input("enter your lastname: "))


    