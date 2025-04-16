name = input("What's your name?")

# if name == "Harry":
#     print("Gryffindor")
# elif  name =="Herminone":
#     print("Gryffindor")
# else:
#     print("Who?")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:     #_ used to accept any input
#         print("Who?")

match name:
    case "Harry"| "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:     #_ used to accept any input
        print("Who?")