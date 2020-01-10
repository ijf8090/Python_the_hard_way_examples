from sys import argv

script, file_name = argv

print("We're going to read %r .", file_name)
#print("If you don't want to do that enter Ctrl-C (^C)")
#print("If you do want to do that, hit RETURN")

#raw_input("?")

print("Opening the file in READ mode")
target = open(file_name, 'r')

print("Reading the file")
print target.read()
print ("Printing text_block = target.read()")
text_block = target.read()


print('And finally we close it')
target.close()
