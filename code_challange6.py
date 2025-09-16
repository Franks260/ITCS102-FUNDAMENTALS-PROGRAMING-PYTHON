print("FACTORIAL PROGRAM")
number=eval(input("Enter a number"))
n1=1
for w in range (number, 1, -1):
    n1 *= w

print("The factorial of",number,"is",n1)