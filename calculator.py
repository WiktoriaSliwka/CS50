x = float(input("What is x? "))
y = float(input("What is y? ")) 
#nested loops. you first see whats in the inner() and then work your way out

#documentation for rounding number / round(number[, ndigits]) /  the square brackets in doc usually mean that the no of digits is optional to specify
#z = int(x) + int(y) #have to put int otherwise it will read it as a string as + joins together

#z = round(x +  y)
#print(f"{z:,}") #add a coma no > 999

z = x /y
print(f"{z:.2f}") # how many digits after decimal point 