def cheese_and_crackers( cheese_count, boxes_of_crackers):
	print(" You have %d cheeses" % cheese_count)
	print(" You have %d boxes of crackers" % boxes_of_crackers)
	print(" That's enough for a party ")
	print(" Get a blanket")
	

cheese_and_crackers( 10, 1000 )

cheese = 1001
boxes  = 19
cheese_and_crackers(cheese, boxes)

cheese_and_crackers(10+10, 1000 - 500)

cheese_and_crackers(cheese + 10+10, boxes + 1000 - 500)

cheese = int(input("How much cheese do you have? "))
boxes  = int(input("How many boxes of crackers do you have? "))
cheese_and_crackers(cheese, boxes)
