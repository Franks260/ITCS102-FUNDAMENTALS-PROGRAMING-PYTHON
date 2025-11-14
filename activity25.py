from activity25_1 import *

name = input("Hello, What is your name?")
print(f"Welcome{name} to my complier")

iscontinue=True

while iscontinue == True:
    print("Please select a program")
    print("A - greet\nB - Factorial\nC - Halftriangle\nE - Exit")

    choice = input("Please enter your choice: ").lower()

    if choice == 'a':
        greet()
        continue
    elif choice == 'b':
        factorial()
        continue
    elif choice == 'c':
        halftriangle()
        continue
    elif choice == 'e':
        print("System exit")
        break
    else:
        print("invalid Choice")