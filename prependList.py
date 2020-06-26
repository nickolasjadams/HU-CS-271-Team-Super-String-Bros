import sys
try :
	prepend = sys.argv[2]
except :
	sys.exit("Must supply string to prepend")

return_str = ""

for line in sys.stdin :
	line = line.strip() # removes additional newline char
	if len(line) > 0 :
		return_str += prepend + " " + line + "\n"

print(return_str)