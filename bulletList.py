import sys

# special unicode chars
bullet = "\U00002022"

return_str = ""

for line in sys.stdin :
	line = line.strip("\n") # removes additional newline char
	if len(line) > 0 :
		# count the indents at the beginning of the line
		if "\t" in line :
			indents = 0
			for char in line :
				if char is not "\t" :
					break
				else :
					indents = indents+1

			return_str += "\t"*indents # reapply indentation for sub bullets
			line = line.strip() # removes tab from input
		return_str += bullet + " " + line + "\n"

print(return_str)