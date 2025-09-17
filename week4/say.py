# import cowsay 
# import sys
# #cowsay is satisfied laptop is just being weird 
# #its asci art 
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])

# #JSON = JavaScript Object Notation 
import sys 
from sayings import hello 
if len(sys.argv) == 2:
    hello(sys.argv[1])