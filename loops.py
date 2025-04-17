#while loops - be careful not to create an infinite loop 
# i = 3
# while i != 0:       # != not equal to operator
#     print("meow!")
#     i = i - 1

# i = 1           #executes operations from right to left but i dont understand why 
# while 1 <= 3:
#     print("meow!")
#     i += 1
#list data type- contains multiple values in the same place

# for i in [0,1,2]:
#     print("meow")

# for i in range(3): #range is better as u dont have to write all the number u can just change the num in the parenthesis 
#     print("meow")

#print ("meow\n" *3, end="")

# while True:
#     n = int(input("What's n?")) 
#     if n > 0:
#         break #allows you to exit a loop when an external condition is met
# for _ in range(n):
#     print("meow")
#range expects an integer
def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
        return n   #have to say return AFTER break to get your value returned after the loop is broken
        
def meow(n):
    for _ in range(n):
        print("meow")