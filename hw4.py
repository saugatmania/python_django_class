
# #TASK 1

# jan = 2200
# feb = 2350
# march = 2600
# april = 2130
# may = 2190

# expense = [2200,2350,2600,2130,2190]

# #1
# Expense_feb = (feb - jan)
# print("Your expense of Febuary is", Expense_feb)
# #2
# First_quarter_expense = (jan+feb+march)
# print("Your first quarter expense is", First_quarter_expense)
# #3
# Exactly = expense.count(2000)
# print("Spent exactly 2000 dollars in any month =", Exactly)
# #4
# expense.append(1989)
# print("Add june expense to my monthly expense", expense)
# #5

# expense[3]=expense[3]-200
# print(expense)

# expense.pop(3)
# print("I returned an item that you bought in a month of April", expense)
# expense.insert(3, 200)
# print(expense)



# #TASK 2

# heros = ['spider man','thor','hulk','iron man','captain america']
# # #1
# # length = len(heros)
# # print(length)
# # #2
# # heros.append("black panther")
# # print(heros)
# # #3

# # heros.insert(3, heros.pop())

# # heros.pop()
# # print(heros)
# # heros.insert(3,"black panther")
# # print(heros)

# # #4
# # heros.remove("thor")
# # heros.remove("hulk")
# # heros.insert(1,"doctor strange")

# heros[1:3] = ["doctor strange"]

# print(heros)
# #5
# heros.sort()
# print(heros)


# #TASK 3

# max_number = int(input("enter any nuber: "))
# add_list = []
# for i in range(1, max_number , 2):
#     add_list.append(i)
# print(add_list)       




# empty_list=[]
# for i in range (5):
#     userinput=int(input("Enter any number: "))
#     empty_list.append(userinput)
# print(empty_list)

# empty_list=sum(empty_list)
# print("The sum of empty list is: ", empty_list)


# mainlist=[]
# evenlist=[]
# oddlist=[]

# for var in range(5):
#     number=int(input("Enter any number: "))
#     mainlist.append(number)
    

#     if number % 2 == 0:
#         evenlist.append(number)
#     elif number % 2 != 0:
#         oddlist.append(number)
    

# print("This is main list: ",mainlist)
# print("this is the oddlist: ",oddlist)
# print("this is the evenlist: ", evenlist)

# mainlist=[]
# evenlist=[]
# oddlist=[]
# duplicatelist=[]

# for i in range(10):
#     num=int(input("Enter any number: "))
#     if num not in mainlist:
#         if num % 2 == 0:
#             evenlist.append(num)
#         else:
#             oddlist.append(num)
#     else:
#         duplicatelist.append(num)
#     mainlist.append(num)

# print(f"mainlist: {mainlist}")
# print(f"evenlist: {evenlist}")
# print(f"oddlist: {oddlist}")
# print(f"duplicatelist: {duplicatelist}")



















