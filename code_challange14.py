
name = input("Enter Your Name : ")
print("Welcome to Odd number compiler, press 0 to end program.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

odd = 0
isContinue = True
total = ""

while isContinue == True:
    number = eval(input("Enter a Number : "))

    if number % 2 == 1:
        print("Odd number detected")
        odd += number
        total += str(number) + ", "
        continue

    elif number == 0:
        print(f"\n{name} has ended the program")
        print(f"Sum of Odd numbers : {odd}")
        print(f"Odd numbers : {total}")
        break

    else:
        print("Even Number, Skip")