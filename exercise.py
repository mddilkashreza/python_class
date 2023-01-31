students = {
    "count": 2,
    "data":[
        {
            "name":"Ram",
            "address":"Tinkune",
            "course": "Python Django",
            "attandance":[
                {
                    "month": "january",
                    "total_working_days": 25,
                    "present":24,
                    "absent": 1,
                    "leave":0,
                },
                {
                    "month": "february",
                    "total_working_days": 28,
                    "present":20,
                    "absent": 2,
                    "leave":6,
                },
            ]
        },

         {
            "name":"Hari",
            "address":"koteshwor",
            "course": "java",
            "attandance":[
                {
                    "month": "january",
                    "total_working_days": 25,
                    "present":23,
                    "absent": 1,
                    "leave":1,
                },
                {
                    "month": "february",
                    "total_working_days": 28,
                    "present":27,
                    "absent": 0,
                    "leave":1,
                }
            ]
        }
        
    ]
}

# print(f"Name: {students.get('name')}")
# education = profile.get("education")
# for education in education:
#     print(f"College: {education.get('college')} and level: {education.get('level')}")

# name = students.get("name")
data = students.get("data")
for data in data:
    print(f"Name: {data.get('name')} , address: {data.get('address')} and course: {data.get('course')}")
    


# address = profile.get("address")
# for address in address:
#     for key, val in address.items():
#         print(key, val.get('ward'))

# attandance = students.get("attendence")
# for attandance in attandance:
#     append.attandance()
#     print(f"month : {attandance.get('month')}")


dates = students.get("data")

if data in dates:
    for data in attandance:
        print(key, val)

       






