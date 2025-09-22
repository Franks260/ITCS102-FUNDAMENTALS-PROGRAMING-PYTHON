print("Multiplication table")
number=eval(input("enter a number: "))
for i in range(1,11,1):
    result = number * i
    print(f"{number} x {i} = {result}")