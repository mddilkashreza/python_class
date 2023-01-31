# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = float(input("Enter your marks: "))


# if(age>=17 and age<=21 and marks>=80):
#     print(name+" is eligible")
# else:
#     print(name+" is not eligible")


# num = int(input("Enter the number: "))
# n = int(input("Enter the power : "))
# result = num**n

# if(result%2==0):
#     print("Result is even.")
# else:
#     print("Result is odd")


# a = int(input("Enter first side :"))
# b = int(input("Enter second side :"))
# c = int(input("Enter third side :"))

# if(c==(a**2 + b**2)**(1/2)):
#     print("Triangle is right angled.")
# if(a==b or a==c or b==c):
#     print("Triangle is isoceles")
# else:
#     print("Triangle is not of known type")


# ch = input("Enter your character :")
# ascii_value = ord(ch)
# if(ascii_value >= 65 and ascii_value<= 90):
#     print("Upper case letter")
# elif(ascii_value>=97 and ascii_value<=122):
#     print("lower case letter")
# else:
#     print("Character is not an alphabet")

# num = int(input("Enter the number of rows:"))
# for i in range(1, num+1):
#     for j in range(1, num-i+1):
#         print(end="")
#     for j in range(i, 0, -1):
#         print(j, end="")
#     for j in range(2,i+1):
#         print(j, end="")
#     print()


# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# rows = int(input("Enter the # of rows:"))
# columns = int(input("Enter the # of columns:"))
# symbol = input("Enter a symbol to use:")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()



# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()

# count = 0
# while count<9:
#     print("Number:", count)
#     count = count+1

# print("Good bye")

# import random
# n = 20
# to_be_guessed = int(n * random.random()) +1
# guess = 0
# while guess != to_be_guessed:
#     guess  = int(input("New number: "))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print("Number too large")
#         elif guess < to_be_guessed:
#             print("Number too small")
#     else:
#         print("Sorry that you are giving up!")
#         break
# else:
#     print("Congratulations. You made it!")

# fruits = [ "Mange", "Grapes", "Apple"]
# for fruits in fruits:
#     print("current fruits:", fruits)

# print("Good bye")


#factorial
num = int(input("Number:"))
factorial = 1

if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
print(factorial)