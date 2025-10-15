dirty = True

while dirty == True:
    confirm = input("Do you want to continue? (yes / no?) ").lower()
    if confirm == 'yes':
        print("cycle continues")
        continue
    elif confirm == 'no':
        print("cycle stops")
        break
    else:
        print("invalid answer")
        continue