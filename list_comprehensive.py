# a = []

# for i in range(5):
#     a.append(i)


# print(a)


# a = [ i for i in range(5)]
# print(a)

# b = [{i: i**3} for i in range(1, 10)]
# print(b)

# c = [{i: i%2} for i  in range (2, 40)]
# print(c)

email = ["1@gmail.com", "2@hotmail.com", "3@gmail.com", "4@yahoo.com", "5@gmail.com"]
gmail_list = [i for i in email if i.endswith("@gmail.com")]
print(gmail_list)