# if > >= < <= == !=

x = int(input("What's x ?"))
y = int(input("What's y ?"))

#good but you can make it more concise 
#elif = else if 
if x < y:
    print("x is less than y")  #boolean expression
elif x >y:
    print("x is greater than y");
else:
    print("x is equal to y") 

#shorter
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#simplified
if x ==y:
    print("x is equal to y")
else:
    print("x is not equal to y")