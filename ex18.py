def print_two(*args):
	arg1,arg2 = args
	print("arg1: %r, arg2: %r" %(arg1,arg2))

def print_three(*args):
	arg1,arg2, arg3 = args
	print("arg1: %r, arg2: %r, arg3: %r" %(arg1,arg2, arg3))

def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" %(arg1,arg2))

def print_one(arg1):
	print("arg1: %r " % arg1)

def print_none():
	print("I got nothing")

def print_none_2():
	print("I STILL got nothing")


print_two("Ian", "Finlay")
print_two_again("Finlay", "Ian")
print_three("Ian", "Joseph", "Finlay")
print_one("Fisrt arg")
print_none();print_none_2();
