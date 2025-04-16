# + - * / %(modulo)
# x = int(input("What's x?"))

# if x % 2 ==0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):  #functional call 
    if n % 2 == 0:  #returns bool value True or False
        return True
    else:
        return False
    

def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0
    
main()