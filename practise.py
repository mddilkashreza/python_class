# num = int(input("Enter any number"))
# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")


# num = int(input("Enter any number"))
# if num % 3 == 0:
#     print("Exatacly divided by 3")

# if num % 5 == 0:
#     print("Exactly divided by 5")

# if num % 7 == 0:
#     print("Exactly divided by 7")

#functional topic

# def welcome():
#     print("I am dilkash reza")

# welcome()
# welcome()

# loop is the process to contiues of work


# a = [11,23,4,4,55,56,7,76,]

# for i in a:
#     print(i)

#range (start:stop:step)
# for i in range(100):
#     print(i)

# total = 0
# for i in range(1, 11):
#     total = total + i
#     print(total)

# total = sum(range(1, 11))

# print(total)

# total = 0
# for i in range(2, 45, 2):
#     total = total + i
#     print(total)

# total = sum(range(2,45, 2))

# print(total)

# total = 5
# for i in range(1, 11):
#     total = total * i


# print(total)

#multipal table
# n = int(input("Enter any number: "))
# for i in range(1, 11):
#     print(n, "*" ,i, "=", n*i)
# n = 6
# for i in range(1, 11):
#      print(n, "*" ,i, "=", n*i)


# for i in range(1, 11):
#     print(7, "*" ,i, "=", 7*i)

# num = int(input("Enter any number"))

# for count in range(1, 11):
#     product = num * count
#     print(num, "*" ,count, "=", product)


# a = int(input("Enter any number "))
# i = 1
# while (i<11):
#     i = i+1
#     print(a,'x' ,i, '=', a*i)
    
# total = 0
# for i in range(2,21,2):
#     total = total + i 
# print(total)

# a = []
# for i in range(6):
#     n = input("Enter your name ")
#     a.append(n.capitalize())
# print(a)

# while condition

# while True:
    # print("I am dilkash")

# a = 0
# while a<5:
#     print("I am ", a)
#     a = a+1
# a = 1 
# while a < 20:
#     if a % 2 == 0:
#         print(a)
#     a = a + 1

# a = 2 
# while a < 20:
#     print(a)
#     a = a + 2

# a = 2
# total = 0
# while a < 20:
#     total = total + a
#     a = a + 2
    


# print(total)

# total = 0
# while a < 50:
#     if n % 3 == 0:

# a = "19d89d43d56"
# b = a.split("d")
# total = 0

# for i in b:
#     total = total + int(i)

# print(total)


# username = input("Enter username ")
# password = input("Enter password ")

# while username != "abc@gmail.com" and password != "12345":
#     username = input("Enter username ")
#     password = input("Enter password ")

# print("Success")

# Break and continue
# for i in range(1, 10):
#     print(i)
#     if i % 5 == 0:
#         break


# while True:
#     a = int(input("Enter number"))
#     if a == 100:
#         break
# for i in range(1, 10):
#     if i % 5 == 0:
#         continue
#     print(i)

# while True:
#     a = int(input("Roll your dice: "))
#     if a == 1 or a == 5:
#         continue
#     else:
#         break


# function

# def welcome():
#     print("I am dilkash reza")

# welcome() # call for function execution
# welcome # call by reference



# def welcome():
#     name = "Dilkash"
#     print("Welcome", name)

# welcome()

# def welcome(name, address): #parament
#     print("Welcome",name)
#     print("Address:", address)

# name = input("Enter your name: ")
# address = input("Enter your address: ")

# welcome(name, address) #agrument

# a = 10
# b = 20 
# total = a + b
# print("The sum of {} and  {} is {}".format(a, b, total))
# print(f"The sum of {a} and {b} is {total}.")

# def profile(name, address, contact):
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"Contact: {contact}")

# profile("Ram","Ktm","876543") #positional arguments
# profile(name="Ram", contact="87654", address="Ktm") #keyword arguments

# def addition(num1, num2):
#     print(num1 + num2)

# addition(10, 20)

# def addition(num1, num2):
#     print(num1 + num2)

# def product(num1, num2):
#     return num1 * num2

# a = addition(10, 20)
# print(f"Addition: {a}")
# res = product(49,3)
# print(f"Product: {res}")

# 30
# Addition: None
# Product: 147

# def multipal_arguments(*a):
#     print(a)

# multipal_arguments(1,2,3,4,5,6,7,8,9, "python", "dilkash")

#main, even, odd, duplicate
# take user input 15 times (int)

# main = []
# even = []
# odd = []
# duplicate = []
# for i in range(15):
#     num = int(input("Enter any number: "))
#     if num in main:
#         duplicate.append(num)
#     else:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     main.append(num)

# print(main)
# print(even)
# print(odd)
# print(duplicate)



# color = ["yellow", "red", "orange", "blue", "violet", "red", "white"]

# while color.count("red",) > 0:
#     color.remove("red")

 
# color.remove("violet")

# print(color) 


# fruits = ["apple", "guava", "grapes", "banana", "orange"]

# fruits[1:3] = ["watermelon"]
# print(fruits)


#Class and Object 


# class Projector:
#     def __init__(self):
#         self.name = "Dilkash"
#         self.address = "Samakhushi"
#         self.contact = 987654321
#         self.college = "Orchid"
#         self.stream  = "BBM"


#     def details(self):
#         print("About Me:") 


#     def information(self):
#         print("To know more about me: ")






# p = Projector()
# print(p.name)
# print(p.address)
# print(p.contact)
# print(p.college)
# print(p.stream)


# class Student:
#     def __init__(self, name, address, contact, college, stream):
#         self.name = name
#         self.address = address
#         self.contact = contact
#         self.college = college
#         self.stream =  stream


#     def details(self):
#         print("About Me: ")

#     def information(self):
#         print("To know more about me: ")


    




# p = Student("Dillkash", "Samakhushi", 987654321, "Orchid", "BBM")
# print(p.name)
# print(p.address)
# print(p.contact)
# print(p.college)
# print(p.stream)

# class Student:
#     def __init__(self, name, address, contact, work, company_name):
#         self.name = name
#         self.address = address
#         self.contact = contact
#         self.work  =  work
#         self.company_name = company_name


#     def details(sefl):
#         print(f"Student of model {self.name} is details")

    

#     def information(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
#         print(f"Contact: {self.contact}")
#         print(f"Work: {self.work}")
#         print(f"Company_name: {self.company_name}")

#     def __str__(self):
#         return self.college

#     def __repr__(self):
#         return self.college

# s1 = Student("Sabirul Ansari", "Sarlahi", 876543, "Labor Helper", "Chandni Workshop")
# s2 = Student("Dilkash", "Samakhusi", 123456789, "banker", "BroadWay")

# # s1.details()

# Student =[]

# for i in range(3):
#     name = input("Enter your name: ")
#     address = input("Enter your address: ")
#     contact = input("Enter your contact number: ")
#     work = input("Enter your work: ")
#     company_name = input("Enter your company_name:  ")
#     s = Student(name, address, contact, work, company_name)
#     Student.append(s)
# print(Student)


# class Student:
#     def __init__(self,  _id, name, contact, address, ):
#         self._id = _id
#         self.name = name
#         self.contact = contact
#         self.address = address
#         self.total_attandance = 0


#     def Update_attandance(self):
#         self.total_attandance += 0


#     def view_attandance(self):
#         return self.total_attandance


# s = Student(1, "Dilkash", "987654321", "Ktm")
# # print(s.view_attandance())
# print(Student.view_attandance(s))


# class Student:
#     def __init__(self, _id, name, contact, address):
#         self._id = _id
#         self.name = name
#         self.contact = contact
#         self.address = address
#         self.total_attandance = 0


#     def Update_attandance(self):
#         self.total_attandance += 1


#     def view_attandance(self):
#         return self.total_attandance


# s = Student(1, "Dilkash", "1234567890", "Ktm")
# s2 = Student(2, "Sabirul", "987654321", "Sarlahi")
# print(s.view_attandance())
# print(s2.view_attandance())
# s.Update_attandance()
# s2.Update_attandance()
# s2.Update_attandance()
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
# # print(tshirt.price())
# # print(tshirt._Product__price)
# # print(jacket._Product__price)
# print(f"Before setting: {tshirt.price}")
# tshirt.price = 2000
# print(f"After setting: {tshirt.price}")
# print(f"Before setting: {jacket.price}")
# jacket.price = 3000
# print(f"After setting: {jacket.price}")


# class Calculator:
#     def __init__(self, num1, num2):
#         self.a = num1
#         self.b = num2

#     def add(self):
#        return self.a + self.b

#     def difference(self):
#         return self.a - self.b

#     def product(self):
#         return self.a * self.b

#     def division(self):
#         return self.a / self.b

#     @staticmethod
#     def square_root(num):
#         return num**0.5



# c = Calculator(30, 3)
# print(c.add())
# print(c.difference())
# print(c.product())
# print(c.division())
# print(Calculator.square_root(625))


# class Calculator:
#     def __init__(self, num1, num2, num3):
#         self.a = num1
#         self.b = num2
#         self.c = num3


#     def add(self):
#         return self.a + self.b + self.c

#     def difference(self):
#         return self.a - self.b - self.c

#     def product(self):
#         return self.a * self.b * self.c

#     def division(self):
#         return self.a / self.b / self.c

#     def square_root(num):
#         return num**0.5


# c = Calculator(30, 3, 2)
# print(c.add())
# print(c.difference())
# print(c.product())
# print(c.division())
# print(Calculator.square_root(625))

# class Student:
#     College = "ABC College"

#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact


# print(Student.College)

# s = Student("Dilkash", "765432")

# print(s.College)
# print(s.__dict__)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def create_usef_with_random_password(cls, username):
        return cls(username, "Default_password")

u = User("dilkash@gmail.com", "Demo3456")
print(u.__dict__)

u2 = User.create_usef_with_random_password("romeyo@gmail.com")
print(u2.__dict__)


        
