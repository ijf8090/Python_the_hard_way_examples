from sys import argv

script, file_name = argv
prompt = "Enter File: "

txt = open(file_name)

print ("Here is your file %r , " % (file_name))
print txt.read()


print("Type the file name again.")
file_name2 = raw_input(prompt)

txt_again2 = open(file_name2)
print ("Here is your file %r , " % (file_name))
print txt_again2.read()
