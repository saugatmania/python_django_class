

# def welcome(name):
#     print(f"Welcome {name}")

# def bye(name):
#     print(f"bye bye {name}")

# def greet_ram(xyz):
#     xyz("ram")

# greet_ram(welcome)
# greet_ram(bye)



# def welcome(name):
#     print(f"Welcome {name}")

# def bye(name):
#     print(f"bye bye {name}")

# def greet_ram(xyz, name):
#     xyz(name)

# greet_ram(welcome, "Hari")
# greet_ram(bye, "Ram")


# def decorate_func(abc):
#     def wrapper():
#         print("before function")
#         abc()
#         print("after function")
#     return wrapper

# @decorate_func
# def demo_func():
#     print("this is function")

# demo_func()

# def smart_vision(func):
#     def wrapper(a,b):
#         if b == 0:
#             return "could not divide by zero"
#         else:
#             return func(a,b)
#     return wrapper

# @smart_vision
# def division(a,b):
#     return a/b

# print(division(10,5))
