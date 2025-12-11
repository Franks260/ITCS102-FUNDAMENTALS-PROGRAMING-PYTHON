import os

name = input("Please enter your name --> ")

print("\n***********************************************************************************")
print(f"HELLO {name} WELCOME TO MY FINALS PROJECT PROGRAM")
print("***********************************************************************************")

while True:
    print("\nWhich work do you want to access?")
    wala = input("A - Activities\nB - Code Challanges\nC - Exit \n---> ").upper()
    os.system('cls')

    if wala =='A':
        print("\t\tYOU CHOOSED ACTIVITIES\n")
        
        print("1  - Activity 1\t\t11  - Activity 11\t21 - Activity 21")
        print("2  - Activity 2\t\t12  - Activity 12\t22 - Activity 22")
        print("3  - Activity 3\t\t13  - Activity 13\t23 - Activity 23")
        print("4  - Activity 4\t\t14  - Activity 13\t24 - Activity 24")
        print("5  - Activity 5\t\t15  - Activity 15\t25 - Activity 25")
        print("6  - Activity 6\t\t16  - Activity 16\t26 - Activity 26")
        print("7  - Activity 7\t\t17  - Activity 17\t27 - Activity 27")
        print("8  - Activity 8\t\t18  - Activity 18\t28 - Activity 28")
        print("9  - Activity 9\t\t19  - Activity 19\tE  - Return to Main Menu")
        print("10 - Activity 10\t20  - Activity 20\n")
        
        activity = input("What Activity you want to view? --> ")
        os.system('cls')

        if activity == "1":
            while True:
                print("************************\n\tACTIVITY 1 \n")
                from activity1 import run1
                run1()
                print("\n************************")
                break

        elif activity == "2":
            while True:
                print("************************\n\tACTIVITY 2 \n")
                from activity2 import run2
                run2()
                print("\n************************")
                break
        
        elif activity == "3":
            while True:
                print("************************\n\tACTIVITY 3 \n")
                from activity3 import run3
                run3()
                print("\n************************")
                break
            
        elif activity == "4":
            while True:
                print("************************\n\tACTIVITY 4 \n")
                from activity4 import run4
                run4()
                print("\n************************")
                break

        elif activity == "5":
            while True:
                print("************************\n\tACTIVITY 5 \n")
                from activity5 import run5
                run5()
                print("\n************************")
                break
            
        elif activity == "6":
            while True:
                print("************************\n\tACTIVITY 6 \n")
                from activity6 import run6
                run6()
                print("\n************************")
                break

        elif activity == "7":
            while True:
                print("************************\n\tACTIVITY 7 \n")
                from activity7 import run7
                run7()
                print("\n************************")
                break
        
        elif activity == "8":
            while True:
                print("************************\n\tACTIVITY 8 \n")
                from activity8 import run8
                run8()
                print("\n************************")
                break
        

        elif activity == "9":
            while True:
                print("************************\n\tACTIVITY 9 \n")
                from activity9 import run9
                run9()
                print("\n************************")
                break

        elif activity == "10":
            while True:
                print("************************\n\tACTIVITY 10 \n")
                from activity10 import run10
                run10()
                print("\n************************")
                break
        
        elif activity == "11":
            while True:
                print("************************\n\tACTIVITY 11 \n")
                from activity11 import run11
                run11()
                print("\n************************")
                break

        elif activity == "12":
            while True:
                print("************************\n\tACTIVITY 12 \n")
                from activity12 import run12
                run12()
                print("\n************************")
                break
            
        elif activity == "13":
            while True:
                print("************************\n\tACTIVITY 13 \n")
                from activity13 import run13
                run13()
                print("\n************************")
                break
        
        elif activity == "14":
            while True:
                print("************************\n\tACTIVITY 14 \n")
                from activity14 import run14
                run14()
                print("\n************************")
                break

        elif activity == "15":
            while True:
                print("************************\n\tACTIVITY 15 \n")
                from activity15 import run15
                run15()
                print("\n************************")
                break

        elif activity == "16":
            while True:
                print("************************\n\tACTIVITY 16 \n")
                from activity16 import run16
                run16()
                print("\n************************")
                break

        elif activity == "17":
            while True:
                print("************************\n\tACTIVITY 17 \n")
                from activity17 import run17
                run17()
                print("\n************************")
                break

        elif activity == "18":
            while True:
                print("************************\n\tACTIVITY 18 \n")
                from activity18 import run18
                run18()
                print("\n************************")
                break

        elif activity == "19":
            while True:
                print("************************\n\tACTIVITY 19 \n")
                from activity19 import run19
                run19()
                print("\n************************")
                break
        
        elif activity == "20":
            while True:
                print("************************\n\tACTIVITY 20 \n")
                from activity20 import run20
                run20()
                print("\n************************")
                break
        
        elif activity == "21":
            while True:
                print("************************\n\tACTIVITY 21 \n")
                from activity21 import run21
                run21()
                print("\n************************")
                break

        elif activity == "22":
            while True:
                print("************************\n\tACTIVITY 22 \n")
                from activity22 import run22
                run22()
                print("\n************************")
                break

        elif activity == "23":
            while True:
                print("************************\n\tACTIVITY 23 \n")
                from activity23 import run23
                run23()
                print("\n************************")
                break

        elif activity == "24":
            while True:
                print("************************\n\tACTIVITY 24 \n")
                
                from activity24 import summation, greet
                name = input("Who do you want to greet? --> ")
                greet(name)
                example = eval(input("Enter A Number you want to sum"))
                summation(example)

                print("\n************************")
                break

        elif activity == "25":
            while True:
                print("************************\n\tACTIVITY 25 \n")
                from activity25_1 import *

                name = input("Hello, What is your name? ")
                print(f"Welcome{name} to my complier")

                iscontinue=True

                while iscontinue == True:
                    
                    print("Please select a program")
                    print("A - greet\nB - Factorial\nC - Halftriangle\nE - Exit")

                    choice = input("Please enter your choice: ").lower()

                    if choice == 'a':
                        os.system('cls')
                        greet()
                        continue
                    elif choice == 'b':
                        os.system('cls')
                        factorial()
                        continue
                    elif choice == 'c':
                        os.system('cls')
                        halftriangle()
                        continue
                    elif choice == 'e':
                        print("System exit")
                        break
                    else:
                        print("invalid Choice")
                        break
                break

        elif activity == "26":
            while True:
                print("************************\n\tACTIVITY 26 \n")
                from activity26 import run26
                run26()
                print("\n************************")
                break

        elif activity == "27":
            while True:
                print("************************\n\tACTIVITY 27 \n")
                from activity27 import run27
                run27()
                print("\n************************")
                break

        elif activity == "28":
            while True:
                print("************************\n\tACTIVITY 28 \n")
                from activity28 import run28
                run28()
                print("\n************************")
                break

    elif wala =='B':
            print("\t\tYOU CHOOSED CODE_CHALLANGES\n")
        
            print("1  - CODE_CHALLANGE 1\t\t11  - CODE_CHALLANGE 11")
            print("2  - CODE_CHALLANGE 2\t\t12  - CODE_CHALLANGE 12")
            print("3  - CODE_CHALLANGE 3\t\t13  - CODE_CHALLANGE 13")
            print("4  - CODE_CHALLANGE 4\t\t14  - CODE_CHALLANGE 13")
            print("5  - CODE_CHALLANGE 5\t\t15  - CODE_CHALLANGE 15")
            print("6  - CODE_CHALLANGE 6\t\t16  - CODE_CHALLANGE 16")
            print("7  - CODE_CHALLANGE 7\t\tE  - Return to Main Menu")
            print("8  - CODE_CHALLANGE 8")
            print("9  - CODE_CHALLANGE 9")
            print("10 - CODE_CHALLANGE 10\n")
    
            cc = input("What CODE_CHALLANGE you want to view? --> ")
            os.system('cls')
            if cc == "1":
                while True:
                    print("************************\n\tCODE_CHALLANGE 1\n")
                    from code_challange1 import cc1
                    cc1()
                    print("\n************************")
                    break

            elif cc == "2":
                while True:
                    print("************************\n\tCODE_CHALLANGE 2\n")
                    from code_challange2 import cc2
                    cc2()
                    print("\n************************")
                    break

            elif cc == "3":
                while True:
                    print("************************\n\tCODE_CHALLANGE 3\n")
                    from code_challange3 import cc3
                    cc3()
                    print("\n************************")
                    break

            elif cc == "4":
                while True:
                    print("************************\n\tCODE_CHALLANGE 4\n")
                    from code_challange4 import cc4
                    cc4()
                    print("\n************************")
                    break

            elif cc == "5":
                while True:
                    print("************************\n\tCODE_CHALLANGE 5\n")
                    from code_challange5 import cc5
                    cc5()
                    print("\n************************")
                    break

            elif cc == "6":
                while True:
                    print("************************\n\tCODE_CHALLANGE 6\n")
                    from code_challange6 import cc6
                    cc6()
                    print("\n************************")
                    break

            elif cc == "7":
                while True:
                    print("************************\n\tCODE_CHALLANGE 7\n")
                    from code_challange7 import cc7
                    cc7()
                    print("\n************************")
                    break

            elif cc == "8":
                while True:
                    print("************************\n\tCODE_CHALLANGE 8\n")
                    from code_challange8 import cc8
                    cc8()
                    print("\n************************")
                    break

            elif cc == "9":
                while True:
                    print("************************\n\tCODE_CHALLANGE 9\n")
                    from code_challange9 import cc9
                    cc9()
                    print("\n************************")
                    break

            elif cc == "10":
                while True:
                    print("************************\n\tCODE_CHALLANGE 10\n")
                    from code_challange10 import cc10
                    cc10()
                    print("\n************************")
                    break

            elif cc == "11":
                while True:
                    print("************************\n\tCODE_CHALLANGE 11\n")
                    from code_challange11 import cc11
                    cc11()
                    print("\n************************")
                    break

            elif cc == "12":
                while True:
                    print("************************\n\tCODE_CHALLANGE 12\n")
                    from code_challange12 import cc12
                    cc12()
                    print("\n************************")
                    break

            elif cc == "13":
                while True:
                    print("************************\n\tCODE_CHALLANGE 13\n")
                    from code_challange13 import cc13
                    cc13()
                    print("\n************************")
                    break

            elif cc == "14":
                while True:
                    print("************************\n\tCODE_CHALLANGE 14\n")
                    from code_challange14 import cc14
                    cc14()
                    print("\n************************")
                    break

            elif cc == "15":
                while True:
                    print("************************\n\tCODE_CHALLANGE 15\n")
                    from code_challange15 import cc15
                    cc15()
                    print("\n************************")
                    break

            elif cc == "16":
                while True:
                    print("************************\n\tCODE_CHALLANGE 16\n")
                    from code_challange16 import cc16
                    cc16()
                    print("\n************************")
                    break


    elif wala =='C':
        print("Exiting program...")
        break
