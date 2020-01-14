from sys import argv

script, file_name = argv

print("We're going to erase %r .", file_name)
#print("If you don't want to do that enter Ctrl-C (^C)")
#print("If you do want to do that, hit RETURN")

#raw_input("?")

print("Opening the file")
target = open(file_name, 'w')

print("Erasing the file")
target.truncate()

print("Now, I'm going to ask you for three lines")
line1 = raw_input("line1 : ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
print('And finally we close it')
target.close()
