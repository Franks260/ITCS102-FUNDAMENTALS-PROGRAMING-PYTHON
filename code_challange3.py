from getpass import getpass
username = input("Enter your username -> ")
password = getpass("Enter your password -> ")

uname = 'Franks'
pwd = 'Pogiako123'

if username == uname and password == pwd :
	print("Access granted")

else:
	print("Access denied")
