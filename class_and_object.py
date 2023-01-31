# object Oriented Programming
# Class and Object
# Encapsulation => data hiding process
# Inheritance 
# Polymorphism
# Abstraction


# class Projector:
#     def __init__(self):
#         self.color = "white"
#         self.year = 2022
#         self.model = "NEC"


#     def visualise(self):
#         print("Visualise")


#     def lightining(self):
#         print("Lightininge")


# p = Projector()
# print(p.color)
# print(p.year)
# print(p.model)

# class Projector:
#     def __init__(self, color, year, model = "NEC"):
#         self.color = color
#         self.year = year
#         self.model = model


#     def visualise(self):
#         print("Visualise")


#     def lightining(self):
#         print("Lightininge")


# p = Projector("White", 2022, "NEC")
# print(p.color)
# print(p.year)
# print(p.model)

# class Projector:
#     def __init__(self, color, year, model = "NEC"):
#         self.color = color
#         self.year = year
#         self.model = model


#     def visualise(self):
#         print(f"Projector of model {self.model} is visualising")


#     def description(self):
#         print(f"Color: {self.color}")
#         print(f"Model : {self.model}")
#         print(f"Yeaf : {self.year}")

#     def __str__(self):
#         return self.model

#     def __repr__(self):
#         return self.model


# p1 = Projector("White", 2022, "NEC")
# p2 = Projector("Red", 2021, "Acer")
# # p1.visualise()
# # p2.visualise()
# # p2.description()
# # print(p1.__dict__)

# projectors = []
# for i in range(3):
#     color = input("Enter color: ")
#     year = input("Enter year: ")
#     model = input("Enter model:")
#     p = Projector(color, year, model)
#     projectors.append(p)

# print(projectors)


class Student:

    def __init__(self, _id, name, contact, address):
        self._id  = _id
        self.name = name
        self.contact = contact
        self.address = address
        self.total_attandance = 0


    def update_attandance(self):
        self.total_attandance += 0


    def view_attandance(self):
        return self.total_attandance

s = Student(1, "Ram", "8776543", "Ktm")
# print(s.view_attandance())
print(Student.view_attandance(s))


# class Student:

#     def __init__(self, _id, name, contact, address):
#         self._id  = _id
#         self.name = name
#         self.contact = contact
#         self.address = address
#         self.total_attandance = 0


#     def update_attandance(self):
#         self.total_attandance +=  1


#     def view_attandance(self):
#         return self.total_attandance

# s = Student(1, "Ram", "8776543", "Ktm")
# s2 = Student(2, "Shyam", "87654", "Bkt")
# s.update_attandance()
# s2.update_attandance()
# s2.update_attandance()
# print(s.view_attandance())
# print(s2.view_attandance())
# print(Student.view_attandance(s))


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price


# tshirt = Product("Tshirt", 500)
# jacket = Product("Jacket", 1000)
# # print(tshirt._Product__price)
# # print(tshirt.price)
# print(f"Before setting: {tshirt.price}")
# tshirt.price = 1122
# print(f"After setting:  {tshirt.price}")

# class Calculator:
#     def __init__(self, num1, num2, num3):
#         self.a = num1
#         self.b = num2
#         self.c = num3


#     def add(self):
#         return self.a + self.b +self.c

#     def difference(self):
#         return self.a - self.b - self.c

#     def product(self):
#         return self.a * self.b * self.c


#     def division(self):
#         return self.a / self.b /self.c

#     @staticmethod 
#     def square_root(num):
#         return num**0.5


# c = Calculator(30, 3, 2)
# print(c.add())
# print(c.difference())
# print(c.product())
# print(c.division())
# print(Calculator.square_root(625))



# class Student:
#     college = "ABC College"

#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact

# print(Student.college)
# s = Student("Ram", "345678")
# print(s.college)
# print(s.__dict__)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    @classmethod
    def create_usef_with_random_password(cls, username):
        return cls(username, "Default_password")

u = User("ram@gmail.com", "Demo12345")
print(u.__dict__)

u2 = User.create_usef_with_random_password("hari@gmail.com")
print(u2.__dict__)
