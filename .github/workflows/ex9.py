days = "Mon Tue Wed Thur Fri Sat Sun"
months = "Jan\nfeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
WHITE = '\n\twgite'

line = "\n\tthis is a line"

very_long_line = """
	This is a long line
A very long line indeed
	in fact you could call it a paragraph
"""

print("Here are the days: %r" % days)
print("Here are the months: %r" % months)
print("Here are the days: %s" % days)
print("Here are the months: %s" % months)


print("\n\n")

#print(" %s", line)
print"\n\t '%s'" % very_long_line
print"\n\t '%r'" % very_long_line
print("It's fleece was %s as snow" % WHITE)
#print("It's fleece was %r as snow" % WHITE)
