#students=["A", "B", "C", "D"]

#houses = ["G", "G", "G", "S"]

# for i in range(len(students)):
#     print(i + 1, students[i])

#dictionary that allows you to associate keys and values with another like words and their definition

# students = {
#     "a" : "g",
#     "b" : "g",
#     "c" : "g",
#     "d" : "s",
#     }

# for student in students:    #named the variable student and the key is students
#     print(student, students[student], sep=",") 

students = [
    {"name": "a", "house": "g", "patronus":"h"},
    {"name": "b", "house": "g", "patronus":"j"},
    {"name": "c", "house": "g", "patronus":"k"},
    {"name": "d", "house": "g", "patronus": None},
]

for student in students:
    print (student["name"], student["house"], student["patronus"], sep=", ")