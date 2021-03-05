#map
#filter
#lambda x,y: x + y

# a = lambda x, y : x + y
# print(a(10,2))


# def increase_by_one(n):
#     return n + 1

# #map(func, iter_object)
# alist = [2,3,4,5,6,7]
# blist = list(map(increase_by_one, alist))
# blist = list(map(lambda n:n+1, alist))
# print(blist)





# email = ["ram_gmail.com", "sita_gamil.com", "hari_gmail.com", "gita_gmail.com"]
# newemail = list(map(lambda e:e.replace("_","@"),email))
# print(newemail)


# namelist = ["ram", "shyam", "hari", "gita", "meera"]
# newname = list(map(lambda e:e.capitalize(),namelist))
# print(newname)

# number = ["12", "17", "18", "21", "65", "89"]
# print(list(map(lambda a:int(a), number)))

#filter

# def is_even(n):
#     return n % 2 == 0

# a = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda n : n % 2 == 0,a))
# print(even)


# email = ["a@gmail.com", "b@gmail.com", "c@test.com", "d@hotmail.com", "e@gmail.com"]
# print(list(filter(lambda email:email.endswith("gmail.com"),email)))