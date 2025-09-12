print("Welcome to manga reader recommender! ")
print("Please answer a few question to find your likings. ")
genre=input("What genre do you like? (action, romance, horror): ")

#ACTION
if genre.lower() == 'action':
    dur=input("How long should the manga be? (short, medium, long,): ")

    if dur.lower() == 'short':
            date=input("Which Decade? (2000, 2010): ")
            if date.lower() == '2000':
                print("I recommend manga to read is SAN")
            else:
                if date.lower() == '2010':
                    print("I recommend manga to read is Tower of God")

    else:
        if dur.lower() == 'medium':
                date=input("Which Decade? (2000, 2010): ")
                if date.lower() == '2000':
                    print("I recommend manga to read is Naruto")
                else:
                    if date.lower() == '2010':
                        print("I recommend manga to read is Gamaran")

        else:
            if dur.lower() == 'long':
                    date=input("Which Decade? (2000, 2010): ")
                    if date.lower() == '2000':
                        print("I recommend manga to read is One Piece ")
                    else:
                        if date.lower() == '2010':
                            print("I recommend manga to read is Gantz ")

#ROMANCE
else:
    if genre.lower() == 'romance':
        dur=input("How long should the manga be? (short, medium, long,): ")
        if dur.lower() == 'short':
            date=input("Which Decade? (2000, 2010): ")
            if date.lower() == '2000':
                print("I recommend manga to read is Beast Master")
            else:
                if date.lower() == '2010':
                    print("I recommend manga to read is Watashitachi no Shiawase na Jikan")
        else:
            if dur.lower() == 'medium':
                date=input("Which Decade? (2000, 2010): ")
                if date.lower() == '2000':
                    print("I recommend manga to read is High School Debut")
                else:
                    if date.lower() == '2010':
                        print("I recommend manga to read is Kimi ni Todoke")
            else:
                if dur.lower() == 'long':
                    date=input("Which Decade? (2000, 2010): ")
                    if date.lower() == '2000':
                        print("I recommend manga to read is Fruits Basket")
                    else:
                        if date.lower() == '2010':
                            print("I recommend manga to read is Horimiya ")

#HORROR
    else:
        if genre.lower() == 'horror':
            dur=input("How long should the manga be? (short, medium, long,): ")
            if dur.lower() == 'short':
                date=input("Which Decade? (2000, 2010): ")
                if date.lower() == '2000':
                    print("I recommend manga to read is Fuan no Tane")
                else:
                    if date.lower() == '2010':
                        print("I recommend manga to read is Souichi's Diary of Curses by Junji Ito")
            else:
                if dur.lower() == 'medium':
                    date=input("Which Decade? (2000, 2010): ")
                    if date.lower() == '2000':
                        print("I recommend manga to read is Shiki")
                    else:
                        if date.lower() == '2010':
                            print("I recommend manga to read is Gannibal by Masaaki Ninomiya")
                else:
                    if dur.lower() == 'long':
                        date=input("Which Decade? (2000, 2010): ")
                        if date.lower() == '2000':
                            print("I recommend manga to read is Manhole by Tetsuya Tsutsui")
                        else:
                            if date.lower() == '2010':
                                print("I recommend manga to read is Portus by Jun Abe ")
