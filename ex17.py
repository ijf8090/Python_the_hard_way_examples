from sys import argv
from os.path import exists
from math import *

print("pi = %s" % pi)
print("All done")

script, from_file, to_file = argv

print("Copying from %s to %s.", from_file, to_file)

in_data = open(from_file).read();
#in_data = in_file.read()

print("The input file is %s bytes long" % len(in_data))
print("Does the output file exist? %r" % exists(to_file))


out_file = open(to_file, 'a+');out_file.write(in_data)
from math import *

out_file.close()
#in_file.close()
