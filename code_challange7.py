print("ODD NUMBER SUMMATION")
num=0

for x in range (1, 11, 1):
    number=eval(input("Enter 10 random number "))
    if number % 2:
        num += number
    
print("The sum of all odd numbers is",num)