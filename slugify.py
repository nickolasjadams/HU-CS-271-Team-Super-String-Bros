import sys, re

return_str = ""

for line in sys.stdin :

	# no line.strip() so we check to make sure this line is just a newline
	if len(line) > 1 : 

		line = line.lower()
		line.replace('\n', '')


		# remove special chars
		line = re.sub(r'[^\w\-_\ \t\n]', '', line)

		if len(line) > 1 :
			# add dash
			line = re.sub(r'\s', '-', line)
		else :
			# special case for lines that only contain special chars
			line = ''
		
		
		return_str += line


print(return_str.rstrip('-'))