
# try:
#     x = int(input("What's x?"))
#     print(f"x is {x}")
# except ValueError:  
#     print("x is not an integer!!")
# #problem - b est programming defensively. think of any future errors 
    
# try:
#     x = int(input("What's x?"))
#     print(f"x is {x}")
# except ValueError:  
#     print("x is not an integer!!")
# #NamError you' re doing something with a variable you should'nt  #the value error is happening too soon so the answer isn't moved to the left

    
# try:
#     x = int(input("What's x?"))
#     print(f"x is {x}")
# except ValueError:  
#     print("x is not an integer!!")
# else:
#     print(f"x is {x}")

#with the else it works better
    
#wile true starts a loop and it asks a boolean expression
    
# while True:
#     try:
#         x = int(input("What's x?"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")
# use break to exit the loop instead of just going to print but it will continue asking you what is x 
# values are stored from right to left

# def main():
#     x = get_int()
#     print(f"x is {x}")

#turning it into a function 
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x?"))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x  #remember to return value !!!

def main():
    x = get_int("What's x? ") #prompting the user for input to make code more reusable
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass

main() #remember to invoke main at the end of the program 