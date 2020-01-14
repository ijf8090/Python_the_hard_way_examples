def add(a,b):
	print("ADDING %d + %d " % (a,b) )
	return a + b


def subtract(a,b):
	print(" SUBTRACTING %d - %d" % (a,b) )
	return a - b


def multiply(a,b):
	print(" MULTIPLYING %d * %d" % (a,b) )
	return a * b


def divide(a,b):
	print(" DIVIDING %d / %d" % (a,b) )
	return a / b

def silly_function():
	print("returning a silly string")
	return "a silly string"

print(" Let's do some math with functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide (100, 2)

print("Age is %d, height is %d ,weight is %d ,iq is %d" % (age, height,weight,iq))

print("Here is a puzzle")
#what = add(age, subtract(height, multiply(weight=180, divide(iq=50,2)=25 )))
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")

returned = silly_function()
print("Reurned==== %s" %returned)
