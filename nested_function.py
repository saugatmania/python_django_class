

# def demo_func():
#     a=10
#     return a

# print(demo_func())


# a=5 #global scope
# def func():
#     a=10#local scope
#     return a
# func()
# print(a)


# def some_func():
#     return 10 
# #call for execution
# #res=some_func()
# #print(res)
# #call by reference
# res=some_func
# print(res())#some_func()

# def outer_func():
#     print("I am outer function")
#     def inner_func():
#         print("I am inner function")
#     return inner_func

# infunc = outer_func()
# infunc()
# infunc()#return garna lai 
# infunc()
# infunc()




# def outer():
#     print("I am outer function")

# def inner():
#     print("I am inner function")


# num1=int(input("enter a number: "))
# num2=int(input("enter another number: "))
# def func(num1,num2):
#     total=num1*num2
    
#     return(total)

# nepal=func(num1,num2)
# nepal   
    # def inner():
    #     total=num1*num2
    #     print(total)    
    # return inner



#closure

def multiplier(n):
    def multiply(a):
        return a * n
    return multiply

times10 = multiplier(10)
del multiplier
print(times10(5))
print(times10(3))


#use of global keyworsd
a = 10 
def func():

    global a 
    a = a + 1
    print(f"value of a: {a}")

func()


alist = []

def func():
    alist.append(5)
    print(alist)

func()


alist = [1,2,3,4]
blist = []
def func():
    blist = alist.copy()
    blist.append(5)
    print(blist)

func()

#nonlocal
def outer():
    a = 10 
    def inner():
        nonlocal a
        a = a + 1
        print(a)
    inner()

outer()
