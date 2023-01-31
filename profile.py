# colors = ["yellow", "red", "orange", "blue", "violet", "red", "white"]
# color to removen= ["red", "violet"]




# color = ["yellow","red","orange","blue","violet","red","white"]


# while color.count("red",) > 0:
#     color.remove("red")

 
# color.remove("violet")

# print(color)  

# fruits = ["apple", "guava", "grapes", "banana", "orange"]
# # replace "guava" and grapes with watermelon

# fruits.remove("guava")
# fruits.remove("grapes")




# print(fruits)


# fruits.append("watermelon")
# print(fruits)

# fruits = ["apple", "guava", "grapes", "banana", "orange"]
# fruits[1:3] = ["watermelon"]
# print(fruits)
profile = {
    "name":"Ram",
    "gender": "Male",
    "education":
    [
        {"college": "ABC College", "level": "+2"},
        {"college": "XYZ College", "level": "Bachelor"},

    ],
    "address":
    [
        {
            "temporary":
            {
            "ward": 1,
            "city":"Kathmandu"
             },
            "parmanent":
            {
            "ward":2,
            "city": "kavre",

             }


        }
    ]
}

print(f"Name: {profile.get('name')}")
print(f"Gender: {profile.get('gender')}")


education = profile.get("education")
for education in education:
    print(f"College: {education.get('college')} and level: {education.get('level')}")

address = profile.get("address")
for address in address:
    for key, val in address.items():
        print(key, val.get('ward'))

