import os
import json
os.system('cls')

print("Student information system")
print("-----------------------------------------------------\n")

#empty directory
student_records = {}

while True:
    print("Select from the options below")
    print("A- Add information")
    print("B- Print Student Record")
    print("C- Search a Record")
    print("D- Delete a Record")
    print("E- Modify a Record")
    print("F- Export Student Record")
    print("G- Import File")
    print("H- Exit System")
    Choice = input("Your Choice -->  ").lower()

    if Choice == 'a':
        print("Adding Student Information")
        print("----------------------------------------------")
        student_id = input("LRN for this student -->  ")
        first_name = input("Input Student First name -->  ").upper()
        last_name = input("Input Student Last Name -->  ").upper()
        course = input("Input Student Course -->  ").upper()
        email = input("Enter email address -->  ")

        student_records[student_id] = [first_name, last_name, course, email]
        print("DATA SAVED")

        os.system('cls')
        continue

    elif Choice == 'b':
        print("Printing Student Record")

        for id, record in student_records.items():
             print(f"Student Id {id} in Student Record {record}")    
        continue

    elif Choice == 'c':
        os.system('cls')
        print("Search Student Record ")
        print("==========================================")

        search_id = input("Input Id to search -->  ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("==============================================")
                print("\n\nRecord Found")
                print("==============================================")
                for i in student_records[search_id]:
                    print(f"-- {i}")

            else:
                print("==============================================")
                print("\n\nNo Record Found")
                print("==============================================")
        continue
    elif Choice == 'd':
        os.system('cls')
        print("Delete Existing Record")
        print("==========================================")

        search_id = input("Input Id to search -->  ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("==============================================")
                print("\n\nRecord Found")
                print("==============================================")
                for i in student_records[search_id]:
                    print(f"-- {i}")

                student_records.pop(search_id)
                print("Record Deleted")

            else:
                print("==============================================")
                print("\n\nNo Record Found")
                print("==============================================")
        continue

    elif Choice == 'e':
        os.system('cls')
        print("EDIT/MODIFY Existing Record")
        print("==========================================")

        search_id = input("Input Id to search -->  ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("==============================================")
                print("\n\nRecord Found")
                print("==============================================")
                for i in student_records[search_id]:
                    print(f"-- {i}")

                student_id = input("LRN for this student -->  ")
                first_name = input("Input Student First name -->  ").upper()
                last_name = input("Input Student Last Name -->  ").upper()
                course = input("Input Student Course -->  ").upper()
                email = input("Enter email address -->  ")

                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = course
                student_records[search_id][3] = email

                print("Record Edited")

            else:
                print("==============================================")
                print("\n\nNo Record Found")
                print("==============================================")
            break
    
    elif Choice == 'f':
        os.system('cls')
        print("Export Student Record")

        with open('student_records.json', 'w') as new_file:
            json.dump(student_records, new_file)
        print("DATA EXPORTED TO json")
        continue

    elif Choice == 'g':
        os.system('cls')
        print("Export Student Record")

        with open('student_records.json', 'r') as new_file:
           student_json = json.load(new_file)

           student_records = student_json
        print("DATA IMPORTED TO json")
        continue


    elif Choice == 'h':
        print("System exit")
        break
    else:
        print("Invalid Choice")