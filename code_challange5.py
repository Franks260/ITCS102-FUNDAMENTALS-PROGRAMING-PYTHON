print("Welcome to manga reader recommender! ")
print("Please answer a few question to find your likings. ")
genre=input("What genre do you like? (action, romance, horror): ")
dur=input("How long should the manga be? (short, medium, long,): ")
date=input("Which Decade? (2000, 2010): ")


#ACTION
if genre.lower() == 'action':
	if dur.lower() == 'short' and date.lower() == '2000':
		print("I recommend manga to read is SAN")
	elif dur.lower() == 'short' and date.lower() == '2010':
		print("I recommend manga to read is Tower of God ")
	elif dur.lower() == 'medium' and date.lower() == '2000':
		print("I recommend manga to read is Naruto")
	elif dur.lower() == 'medium' and date.lower() == '2010':
		print("I recommend manga to read is Gamaran")
	elif dur.lower() == 'long' and date.lower() == '2000':
		print("I recommend manga to read is One Piece ")
	elif dur.lower() == 'long' and date.lower() == '2010':
		print("I recommend manga to read is Gantz ")
	else:
		print("Please enter the choices carefully")


#ROMANCE
elif genre.lower() == 'romance':
	if dur.lower() == 'short' and date.lower() == '2000':
		print("I recommend manga to read is Beast Master")
	elif dur.lower() == 'short' and date.lower() == '2010':
		print("I recommend manga to read is Watashitachi no Shiawase na Jikan")
	elif dur.lower() == 'medium' and date.lower() == '2000':
		print("I recommend manga to read is High School Debut")
	elif dur.lower() == 'medium' and date.lower() == '2010':
		print("I recommend manga to read is Kimi ni Todoke")
	elif dur.lower() == 'long' and date.lower() == '2000':
		print("I recommend manga to read is Fruits Basket")
	elif dur.lower() == 'long' and date.lower() == '2010':
		print("I recommend manga to read is Horimiya ")
	else:
		print("Please enter the choices carefully")


#HORROR
elif genre.lower() == 'horror':
	if dur.lower() == 'short' and date.lower() == '2000':
		print("I recommend manga to read is Fuan no Tane")
	elif dur.lower() == 'short' and date.lower() == '2010':
		print("I recommend manga to read is Souichi's Diary of Curses by Junji Ito")
	elif dur.lower() == 'medium' and date.lower() == '2000':
		print("I recommend manga to read is Shiki")
	elif dur.lower() == 'medium' and date.lower() == '2010':
		print("I recommend manga to read is Gannibal by Masaaki Ninomiya")
	elif dur.lower() == 'long' and date.lower() == '2000':
		print("I recommend manga to read is Manhole by Tetsuya Tsutsui")
	elif dur.lower() == 'long' and date.lower() == '2010':
		print("I recommend manga to read is Portus by Jun Abe ")
	else:
		print("Please enter the choices carefully")
	
else:
	print("Please enter the choices carefully")
