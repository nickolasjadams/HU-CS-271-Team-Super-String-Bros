import sys

return_str = ""

for line in sys.stdin :
	line = line.strip("\n") # removes additional newline char
	if len(line) > 0 :

		for x in range(len(line)-1, -1, -1) :

			return_str += line[x]

print(return_str, end = '')