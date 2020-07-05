import sys, string, random, re

# int length
def generateUID(length) :
	length = int(length)
	legal_chars = ''.join(string.ascii_letters + string.digits)
	uid=""

	for i in range(0, length) :
		uid += random.choice(legal_chars)

	return uid