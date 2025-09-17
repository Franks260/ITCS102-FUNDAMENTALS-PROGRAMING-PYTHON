print("MULTIPLICATION TABLE MAKER")
number=eval(input("Enter a number: "))

print("\nMultiplication table for",number,":")

for x in range (1, 11):
    result = number * x
    print(number,"x",x,"=",result)