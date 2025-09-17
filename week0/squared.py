def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    #return n * n 
    #return n ** 2  # two * means number of the left by the power of the right
    return pow(n, 2) # built in power function
main()