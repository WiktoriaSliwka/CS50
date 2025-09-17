#Files I/O. Sorting information persistently so that when you return all information will be stored.
# names = []

# for _ in range(3):
#     names.append(input("What's your name?"))

# for name in sorted (names):
#     print(f"hello, {names}")

# ***************** #

# name = input("What's your name? ")

# file = open("names.txt", "a") #w is for write so that open knows what file to handle / a for append. 
# file.write(f"{name}\n")
# file.close()

 # we are writing directly into the file and saving but it can delete the past info as we are not appending/ When we re-write the file it will recreate a new file 
# rm names.txt (rm removes the files can be used for different files)
#need to add new line or it will conjoin all the text \n

# ****** #
# name = input("What's your name? ")

# with open("names.txt", "a") as file: 
#     file.write(f"{name}\n")

# ********* #
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())
#**********#

# Organize data in file  
#create list
names = [] 

#iterate list
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) #append to the list not the memory #RSTRIP strips the end of the new line 

#sort list 
for name in sorted(names, reverse=True): # reversed=True organizes in descending order
    print(f"hello, {name}")

#****#

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())

#****#
 
#csv = comma separated value 
# View the comma as a separate column 