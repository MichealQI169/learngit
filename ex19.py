def cheese_and_cracker(cheese_count,boxs_of_crackers):
	print(f"You have {cheese_count} cheese!")
	print(f"You have {boxs_of_crackers} box of crackers!")
	print("Man that enough for a party!")
	print("Get a blanket.\n")
	

print("We can just give the function numbers directly:")
cheese_and_cracker(20,30)


print("Or ,we can use variables from our script:")
amount_of_cheese = 10
amount_of_cracker = 50

cheese_and_cracker(amount_of_cheese,amount_of_cracker)

print("We can do math inside too:")
cheese_and_cracker(10+20,5+6)

print("And we can combine the two,variables and math:")
cheese_and_cracker(amount_of_cheese + 10, amount_of_cracker + 30)
