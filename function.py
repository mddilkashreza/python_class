# def welcome():
#     print("Welcome everyone to function class")
# welcome()
# welcome()
# welcome()

# def welcome():
#     print("welcome students!")

# welcome() #call for function execution
#welcome call by reference

# def welcome(name, address): #parameters
#     print("welcome", name)
#     print("Address:", address)

# name = input("Enter your name")
# address = input("Enter your address:")
# welcome(name, address) #arguments

# a = 10
# b = 20
# total = a + b
# # print("The sum of {} and {} is {}".format(a, b, total))
# print(f"The sum of {a} and {b} is {total}.")

# def profile(name, address, contact):
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"Contact: {contact}")

# profile("Ram" , "Ktm", "987654321") #positional arguments 
# profile("Ram", "987654321", "ktm")
# profile(contact="9876", name="Dilkash", address="samkhushi")


# def addition(num1, num2=1):
#     print(num1+num2)

# addition(10, 5)

# def addition(num1, num2):
#     print(num1 + num2)

# def product(num1, num2):
#     return num1 * num2

# a = addition(10, 20)
# print(f"Addition: {a}")
# res = product(10, 5)
# print(f"Product: {res}")

# def multiple_arguments(*a):
#     print(a)

# multiple_arguments(1,2,3,4,5,6,7,8, "python", "Ram")

# main = []
# even = []
# odd = []
# duplicate = []
# for i in range(15):
#     num = int(input("Enter any number:"))
#     if num in main:
#         duplicate.append(num)
#     else:
#         if num % 2 == 0:
#             even.append(num)
#         odd.append(num)
#     main.append(num) 

# print(main)
# print(even)
# print(odd)
# print(duplicate)   


def multiple_keyword_argument(**k):
    print(k)


multiple_keyword_argument(name="Ram", contact="56789", address="76543", _id=68)




    

