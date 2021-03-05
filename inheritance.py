

# class Bird:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def fly(self):
#         print(f"{self.name} is flying.")


# class pigeon(Bird):
#     def __init__(self, name, color):
#         #Bird.__init__(slef, name)
#         super().__init__(name, color)

#     def fly(self):
#         super().fly()
#         print(f"{self.name} of {self.color} color is flying above.")

# class ostrich(Bird):
#     def __init__(self,name, color):
#         super().__init__(name,color)

#     def fly(self):
#         print(f"{self.name} could not fly.")


# p = pigeon("saugat", "white")
# p.fly()
# # print("pigeon", p.name, p.color)
# o = ostrich("chetan", "grey")
# o.fly()
# # print("ostrich", o.name, o.color)


class User:
    def __init__(self, _id, username, password):
        self._id = _id
        self.username = username
        self.password = password

    def login(self, username, password):# student and teacher should be able to login
            if self.username == username and self.password == password:
                print("logged in")
            else:
                print("error")

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
        print(f"Id: {self._id}")
        print(f"username: {self.username}")
        print(f"name: {self.name}")
        print(f"contact: {self.contact}")
        print(f"address: {self.address}")


class Student(Person):
    def __init__(self, _id, username, password, name, contact, address, course):
        super().__init__(_id, username, password, name, contact, address)
        self.course = course

    def display_profile(self):
        super().display_profile()
        print(f"course: {self.course}")

class Teacher(Person):

    def __init__(self, _id, username, password, name, contact, address, designation):
        super().__init__(_id, username, password, name, contact, address)
        self.designation = designation

    def display_profile(self):
        super().display_profile()
        print(f"designation: {self.designation}")


st = Student("001", "ram", "ram123", "Ram", 877688, "ktm", "Python")
# te = Teacher("004", "haru", "hari123", "Hari", 943443, "pkr", "co-ord")
uname = input("enter username: ")
pwd = input("enter password: ")
st.login(uname, pwd)
# te.login(uname, pwd)
st.display_prw
# st.display_profile()



