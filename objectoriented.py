
# class Car:
#     # initialiser function
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def start(self):
#         print(f"{self.model} started")

# bmw = Car("black", "BMW001")
# print(bmw.__dict__)
# bmw.start()
# audi = Car("red", "audi01")
# print(audi.__dict__)
# audi.start()
# mer = Car("white", "amg001")
# print(mer.__dict__)
# mer.start()


# class Product:

#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price    #Name mangaling

#     def get_current_price(self):
#         return self.__price

# tshirt = Product("T-Shirt", 1000)
# # tshirt.price = 500
# # print(tshirt.price)
# print(tshirt.__dict__)


# class Product:

#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price    #Name mangaling

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price
#         else:
#             raise ValueError("Price can not be less than zero")


# tshirt = Product("T-Shirt", 1000)
# print("Price before: ",tshirt.price)
# try:
#     tshirt.price = 500
# except ValueError as err:
#     print(err)
# print("Price after: ",tshirt.price)



# class student:
#     #sttic or class variable
#     collage_name = "abc collage"
#     def __init__(self,_id,name):
#         #instant variable
#         self._id = _id
#         self.name = name

# st = student("001","ram")
# st2 = student("002","shyam")
# print(st2.collage_name)

# class calculator:
    
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1 + self.num2

#     def difference(self):
#         return self.num1 - self.num2

#     @staticmethod
#     def square_root(num):
#         return num ** 0.5


# c = calculator(10,20)
# print(c.add())
# print(c.difference())
# a = int(input("enter a number: "))
# print(calculator.square_root(a))

# class product:

#     def __init__(self, name, price,qty):
#         self.name = name
#         self.__price = price    #Name mangaling
#         self.qty  = qty

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price
#         else:
#             raise ValueError("Price can not be less than zero")
#     def __str__(self):
#         return f"{self.name}/{self.price}"

#     def __eq__(self,obj):
#         return self.qty == obj.qty


# tshirt = product("tshirt",1000,5)
# pant = product("pant",1500,6)
# shoes = product("shoes",2000,6)


# print(tshirt)
# print(pant)
# print(shoes)

# print(shoes == pant)

