#python interpreter just write //python// in terminal to open interactive mode


#print("Hello world!")  #built in function
# an argument is an input to a function that somehow influences its behavior 
# () parentheses
# a bug is a mistake 

#name = input("what's your name g? ")
#print("Hello, " + name + "!")

#print(*objects, sep='', end='\n', file=sys.stout, flush=false)  sep is separator so can be what u want in between words end could be new line or nothing 

#print("Hello, ", end="")
#print(name + " !")
#print("hello, \"friend\"") #if u want to add quotations within a quotation 
#remove whitespace from str
#name = name.strip()

#Capitalize users name
#name = name.title()

#remove whitespace and capitalize by joining methods
#name = name.strip().title()

#f =format string
#print(f"hello, {name}!")
name = input("what's your name g? ").strip().title()

#split users name into first and last name
first, last = name.split(" ")
print(f"hello, {first}")