def greet(name):
    print(f"Hello {name} welcome and have a nice day")

def factorial(num):
    fact = 1 
    for x in range(num,0,-1):
        fact *= x
    return fact

def halftriangle():
    for i in range(11,1,1):
        for x in range(i,1,1):
            print("",end=" ")
    print()