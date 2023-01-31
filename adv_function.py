# def greet():
#     print("Hello Students!")
#     print("Welcome everyone!")

# g = greet
# g() 





# def addition(num1, num2):
#     print(num1 + num2)

# a = addition
# a(19, 38)

# def sub(num1, num2):
#     print(num1 - num2)

# a = sub 
# a(43, 8)

# def outer():
#     def inner():
#         print("I am inner function")
#     inner()


# outer()

# def calculator():
#     def addition(num1, num2):
#         print(num1 + num2)
#     return addition



# add = calculator()
# add(15, 20)


# def calculator(operator):
#     def addition(a,b):
#         return a + b 
#     def difference(a,b):
#         return a - b 
#     def product(a,b):
#         return a * b
#     if operator == "+":
#         return addition
#     if operator == "-":
#         return difference
#     if operator == "*":
#         return product



# a = calculator("+")
# print(a(20, 10))

#closure 
 
# def increment(num):
#     def factor(val):
#         return num + val 
#     return factor



# increase_by = increment(20)
# print(increase_by(0))
# print(increase_by(50))


# def welcome(name):
#     print(f"Welcome {name}")

# def bye_bye(name):
#     print(f"Bye bye {name}")

# def greet(func):
#     func("Ram")

# greet(bye_bye)

# def decorate_function(func):
#     def wrapper():
#         print("Hello everyone!")
#         func()
#         print("Bye everyone!")
#     return wrapper


# @decorate_function
# def welcome():
#     print(f"Welcome everyone!")


# # w = decorate_function(welcome)
# # w()


# welcome()

# def smart_division(func):
#     def wrapper(a, b):
#         if b == 0:
#             return "could not divide by zero"
#         else:
#             return func(a,b)
#     return wrapper

# @smart_division
# def division(a, b):
#     return a / b

# #print(division)
# print(division(20, 10))
# print(division(20, 0))

# import time

# start_time = time.time()
# total = 0
# for i in range(1, 1000000001):
#     total += i 


# print(total)
# print(time.time() - start_time)


# import time

# start_time = time.time()

# def smart(func):
#     def wrapper(a, b):
#          if b == 0:
#              return "could not divide by zero"
#          else:
#              return func(a,b)
#     return wrapper

# @smart
# def division(a, b):
#      return a / b

#  #print(division)
# print(division(30, 10))
# print(division(20, 10))
# print(time.time() - start_time)

# import time

# def execution_time(fn):
#     def wrapper():
#         start_time = time.time()
#         fn()
#         print(time.time() - start_time)
#     return wrapper

# @execution_time
# def example():
#     print("Hello everyone")

# example()
   


