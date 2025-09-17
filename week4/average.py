#python comes with a statists module
#sys= system sys.argv = argument vector 
# import statistics

# print(statistics.mean([100, 90]))

import sys

# try:
#     print("hello, my name is ", sys.argv[1]) #write argument on print line (python average.py name)
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is ", sys.argv[1])
    #else has to be the last statement, u cant have multiple else statements 


# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2: #len = length of argument
#     sys.exit("Too many arguments")
# #program exits so there wont be an issue

# print("hello, my name is ", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # need to start at location 1 not 0 or it will print average.py and u need a : to show end of list(leave blank )
    print("hello, my name is", arg)

#third party libraries are called packages which is a module in a folder. pypi.org - packages 
#cowsay package
#pip is a package manager 