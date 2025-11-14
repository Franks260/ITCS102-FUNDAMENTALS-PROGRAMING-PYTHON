print("Adding data to dictionary")
print("===================================================")
tuloy=True

empty_dictionary = {}

def print_anime():
        for i,j in empty_dictionary.items():
                print(f"Code -- {i} Title -- {j}")

def pang_search():
        print("Searching ...")
        print(f"Result shows {empty_dictionary[keys].upper()} on our database")

# def print_anime():
#         for anime in empty_dictionary.values():
#                 print(f"Anime -- {anime}")

while tuloy == True:
        keys = input("input keys for this anime  ")

        value = input("Enter anime title ----->  ")

        empty_dictionary[keys] = value

        choice = input("Do you want to continue adding anime\ny - Yes\nn - No\np - Print\ns - Search  ").lower()

        if choice == 'y':
                print("Continuing...")
                continue
        elif choice == 'n':
                print("Program stops")
                break
        elif choice == 'p':
                print_anime()
                continue
        
        elif choice == 's':
                code = input("Enter code for anime to search -->")
                pang_search()
                continue
        else:
                print("Invalid Choice")