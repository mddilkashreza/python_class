#Child class "IS A" Parent class
#Teacher "IS A" Person => this is correct
#Dog "IS A" Person => this is incorrect


# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address


#     def walk(self):
#         print(f"{self.name} is walking")



# class Teacher(Person):
#     def __init__(self, name, address, designation):
#         super().__init__(name, address)
#         self.designation = designation


#     def teach(self):
#         print(f"{self.name} is teaching.")

# #add
# class Student(Person):
#     def __init__(self, name, address, roll_number):
#         super().__init__(name, address)
#         self.roll = roll_number

#     def walk(self):
#         # super().walk()
#         print(f"{self.name} is running.")



# t = Teacher("Ram", "Ktm", "prof")
# t.walk()
# t.teach()





# class User:
#     def __init__(self, username, password):
#         self.name = username
#         self.password = password


# class Person(User):
#     def __init__(self, username, password, name, address):
#         super().__init__(username, password)
#         self.name = name
#         self.address = address
#         self.username = username


#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
#         print(f"Username: {self.username}")


# class Student(Person):
#     def __init__(self, username, password, name, address, rollno):
#         super().__init__(username, password, name, address)
#         self.roll_number = rollno

# class Teacher(Person):
#     def __init__(self, username, password, name, address, designation):
#         super().__init__(username, password, name, address)
#         self.designation = designation

# s = Student("ram@gmail.com", "1234", "Ram", "Ktm", 1)
# s.profile()

# print("*"*50)

# t = Teacher("t@gmail.com", "678", "mine", "ktm", "prof")
# t.profile()


class ProductPriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ProductPriceError("price can not be less than zero.")
        self.__price = price

tshirt = Product("Tshirt", 500)
try:
    tshirt.price = -100
    print(f"Without exception:{tshirt.price}")  
except ProductPriceError as msg:
    print(msg)
    print(f"After exception: {tshirt.price}")      