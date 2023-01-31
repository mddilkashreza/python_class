#map, filter 
# lambda

#map (func, iterable_objects)

# a = [ 3, 9, 8, 17, 15, 90]

# def increase_by_one(n):
#     return n+1



# output = list(map(increase_by_one, a ))
# print(output)

# name_list = ["ram", "shyam", "sita", "meera", "hari"]

# out = list(map(lambda n:n.capitalize(), name_list))
# print(out)

# output = list(map(str.capitalize, name_list))
# print(output)

#filter(func, iterable_object)
#this function should always return boolean value

# a = [ 1,2,3,4,5,6,7,8,9,10]

# out = list(filter(lambda n:n % 2 == 0, a))
# print(out)

# a = "2,4,6,d,8,9,e,4"

# # print(sum(map(int, filter(str.isdigit,a.split(",")))))

# num_list = a.split(",")
# numbers = filter(str.isdigit,num_list)
# print(sum(map(int, numbers)))

marks_of_students = [
    {
        "name": "Ram",
        "marks":
            {"maths": 80, "science": 85, "computer":90},
        
    },
     {
        "name": "Sita",
        "marks":
            {"maths": 87, "science": 79, "computer":85},
        
    },
     {
        "name": "Hari",
        "marks":
            {"maths": 90, "science": 75, "computer":88},
        
    },
]

for m in marks_of_students:
    print(m.get("name"))
    print(sum(m.get("marks").values()))

+++++++++++