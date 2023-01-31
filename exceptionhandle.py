# a = int(input("enter any number"))
# b = int(input("enter any number"))

# total = a + b
# print(total)

# try:
#     #block of code
# except Exception:
#     #block of code
# except TypeError:
#     # block of code
# else:
#     # block of code
# finally:
#     # block of code


# use of try and except
try:
    a  = int(input("enter any number "))
    b  = int(input("enter another number "))

    print(f"sum of {a} and {b} is {(a+b)}.")
except ValueError:
    print("Can not convert to integer.")

name = input("Enter your name: ")
print(f"Name: {name}")




# use of else
try:
    a  = int(input("enter any number "))
    b  = int(input("enter another number "))

    
except ValueError:
    print("Can not convert to integer.")

else:
    print(f"sum of {a} and {b} is {(a+b)}.")

name = input("Enter your name: ")
print(f"Name: {name}")