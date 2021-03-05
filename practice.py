# def calculator():

    

#     if math == "+":
#         print("You enter addition and your answer is" , num1 + num2)
#     elif math == "-":
#         print("You enter subtraction and your answer is" , num1 - num2)
#     elif math == "*":
#         print("You enter multiplication and your answer is" , num1 * num2)
#     elif math == "/":
#         print("You enter division and your answer is" , num1 / num2) 


# num1=int(input("enter a number: "))
# num2=int(input("enter another number: "))
#     math=input("enter a arthemetic operator: ")  

   
# calculator()


# def a(x,y):
#     return x + y

# def b(x,y):
#     return x - y

# def c(x,y):
#     return x * y

# def d(x,y):
#     return x / y

# x = int(input("enter a number: "))
# y = int(input("enter a nother number: "))

# print(" + for add\n", "- for sub\n", "* for mul\n", "/ for div")

# your_choice = input("your choice: ")

# if your_choice == "+":
#     print(a(x,y))

# elif your_choice == "-":
#     print(b(x,y))

# elif your_choice == "*":
#     print(c(x,y))

# elif your_choice == "/":
#     print(d(x,y))

# else:
#     print("ERROR")


# def username(a,b):
#     return "you have enter correct "



# username=input("enter your user name: ")
# password=input("enter your password: ")

# if username == "":
#     print("you are logged in", username())

# elif password == "basnet":
#     print("you are logged in", username())

# else:
#     print("error")



# def logIn(a,b):
    

#     if username == "saugat":
#         pass
#         if password == "basnet":
#             print("you are logged in!",a)

#         else:
#             print("Your password is incorrect",b)

#     else:
#         print("ERROR")

#     return logIn

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# logIn(username,password)


# def multi(n):
#     def inner(a):
#         return n * a 
#     return inner

# outer = multi(10)
# print(outer(5))



# def outer():

#     def inner():
#         return "i am inner"
#     print(("i am outer ") + inner())
    
#     inner()
    
# outer()

# a = 10
# def outer():
    
#     global a
#     a = a + 1 
#     print(a)

# outer()

# alist = [ 1,2,3,4]

# def outer():
#     alist.append(5)
#     print(alist)
# outer()


# def outer():
#     a = 10
#     def inner():
#         nonlocal a 
#         a = a + 1 
#         print(a)
#     inner()
# outer()

# def a(outer):
#     def b():
#         print("before function")
#         outer()
#         print("after function")
#     return b 

# @a
# def c():
#     print("this is function")
# c()

# def a(name):
#     print("my name is", name)

# def b(name):
#     print("my first name is",name)

# def c(hello):
#     hello("saugat")

# c(a)
# c(b)


# def a(func):
#     def b(x,y):
#         if x == 0:
#             return "zero cant be divisible by any number"
#         else:
#             return func(x,y)
#     return b

# @a
# def c(x,y):
#     return y/x

# print(c(10,2))
# print(c(0,10))



# def outer(func):
#     def inner():
#         print("print this at first")
#         func()
#         print("print this at last")
#     return inner

# @outer
# def num():
#     print("this is pyhton")
#     print("this is decorator")
# num()


# def math(abc):
#     def add():
#         a = abc()
#         ok = a + 5
#         return ok
#     return add
# @math
# def num():
#     return 10
# print(num())

# def a(xyz):
#     def b():
#         x = xyz()
#         y = x + 40
#         return y 
#     return b 

# @a
# def c():
#     return 10
# print(c())
    
# a = lambda x,y:x*y
# print(a(5,10))

# b = lambda a,b,c : a * b - c
# print(b(5,5,5))

# def a(n):
#     return n + 1

# alist = [1,2,3,4,5,6,7,8,9]
# blist = list(map(a,alist))
# print(blist)

# def b(n):
#     return n * 5

# alist = [1,2,3,4,5,6,7,8,9,10]
# blist = list(map(b,alist))
# print(blist)


# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# # def b(n):
# #     if n>= 10:
# #         return True

# aresult = list(filter(lambda a:a >= 10,a))
# print(aresult)

# for i in aresult:
#     print(i)


# class house():

#     def __init__(self,price,color):
#         self.price = price
#         self.color = color

    # def booked(self):
    #     print(f"{self.color} house haved been booked")

    # def available(self):
    #     print(f"{self.color} house is available")


# a = house("3cr","red")
# print(a.__dict__)
# a.booked()

# b = house("4cr","white")
# print(b.__dict__)
# b.available()

# c = house("5cr","yellow")
# print(c.__dict__)
# c.booked()

# d = house("4cr","green")
# print(d.__dict__)
# d.available()

# e = house("4cr","blue")
# print(b.__dict__)
# e.available()

# class a ():

#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price

#     def b(self):
#         return self.__price

# tshirt = a("tshirt",1000)
# print(tshirt.__dict__)
# # print(tshirt.b())
# print(tshirt._a__price)
# print(tshirt_a__name)


# class product():

#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
    
    
#     def a(self):
#         return self.name
#     def price(self):
#         return self.__price
    

# tshirt = product("tshirt",1000)
# print(tshirt.__dict__)
# print(tshirt.a())
# print(tshirt.price())
# print(tshirt._a__price)
# print(tshirt_a__name)


class User:
    def __init__(self, _id, username, password):
        self._id = _id
        self.username = username
        self.password = password

    def login(self, username, password):# student and teacher should be able to login
            if self.username == username and self.password == password:
                print(f"Welcome {self.username}")
            else:
                print("ERROR")

class Person(User):
    def __init__(self, _id, username, password, name, contact, address):
        super().__init__(_id, username, password)
        self.name = name
        self.contact = contact
        self.address = address

    def display_profile(self):
        """
        _id, username, name, contact, address
        if object is student -> also print course
        if object is teacher -> also print designation
        """
        # print(f"Id: {self._id}")
        # print(f"username: {self.username}")
        # print(f"name: {self.name}")
        # print(f"contact: {self.contact}")
        # print(f"address: {self.address}")
        print(f"Id: {self._id}")
        print(f"Username: {self.username}")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Address: {self.address}")


class Student(Person):
    def __init__(self, _id, username, password, name, contact, address, course):
        super().__init__(_id, username, password, name, contact, address)
        self.course = course

    # def display_profile(self):
    #     super().display_profile()
    #     print(f"course: {self.course}")

class Teacher(Person):

    def __init__(self, _id, username, password, name, contact, address, designation):
        super().__init__(_id, username, password, name, contact, address)
        self.designation = designation
    






