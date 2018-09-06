people = 30
cars = 40
trucks = 15


if cars > people:
	print("we should rake the cars.")
elif cars < people:
	print("we should not take the cars")
else :
	print ("we can decide")
	
if trucks > cars:
	print("That too many trucks")
elif trucks < cars:
	print("maybe we could take the trucks.")
else :
	print("we still can't decide")
	
if people > trucks:
	print("Alright ,let's just take the trucks.")
else :
	print("Fine, let's stay home then.")
	
