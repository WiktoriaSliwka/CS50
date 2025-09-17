#rows contain the information split by coma so you can call a specific row
# with open("students.csv") as file:
#     for line in file:
#         row= line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")


#*********#
#code does the same as above but now its more readable 
# with open("students.csv") as file:
#     for line in file:
#         name, house= line.rstrip().split(",")
#         print(f"{name} is in {house}")


#******# 

# students= []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}") 

# for student in sorted(students):
#     print(student)


#csvs can cause issues with larger data so best to import python module csv 
# import csv

# students= []

# with open("students.csv") as file:
#     reader = csv.reader(file) # iterate over reader not FILE
#     for name, home in reader:
#         students.append({"name": name, "home": home})


#  #Lambda is an anonymous function because you dont need to give it a name 
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']}is in {student['house']}")

# # dictreader
# #first row has to be the name of the row which helps avoid mistakes.    
# import csv

# students= []

# with open("students.csv") as file:
#     reader = csv.DictReader(file) # iterate over reader not FILE
#     for name, home in reader:
#         students.append({"name": name, "home": home})


#  #Lambda is an anonymous function because you dont need to give it a name 
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']}is in {student['house']}")

import csv
name = input("What's your name?")
home =  input("Where's your home?")

with open("students.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow({"name":name, "home": home})
    