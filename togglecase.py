import sys, random

return_str = ""
return_str_randomized = ""

for line in sys.stdin :
	line = line.strip() # removes additional newline char
	if len(line) > 0 :
		return_str = line.lower() + "\n"

		# randomly uppercase 
		for char in range(len(return_str)) :
			r = random.randint(0, 2)

			if r == 0 :
				return_str_randomized += return_str[char].upper()
			else :
				return_str_randomized += return_str[char]

print(return_str_randomized)