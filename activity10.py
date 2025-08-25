name = input("Input your name here ")
isStudent = input("Are you a student? yes or no ")
fare = eval(input("How much is your fare? "))

if isStudent.lower() == "yes" :
	discount = fare * .2
	new_fare = fare - discount
	print("Hi",name,"your discounted fare is",new_fare)
else:
	print("Sorry discount is only eligible for student")