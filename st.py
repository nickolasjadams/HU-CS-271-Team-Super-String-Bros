import sys


num_args = len(sys.argv)

# options lists
help_keys = ["--help", "-h", "help"]
bullet_list_keys = ["bullet-list", "ST-1"]
prepend_list_keys = ["prepend-list", "ST-2"]
slugify_keys = ["slugify", "ST-3"]
uid_keys = ["uid", "ST-4"]
togglecase_keys = ["togglecase", "memecase", "spongebob", "mock", "ST-5"]
reverse_keys = ["reverse", "backwards", "ST-6"]


version_info = """
Welcome to String Tools
 -- developed by The Super String Bros

version: 1.0.0
Usage: python3 st.py [story key or feature name]
--help or -h to view features
"""

help_info = """
Usage: python3 st.py [story key or feature name]

	bullet-list ST-1 - Convert a common separated list to a bulleted list

	prepend-list ST-2 - Prepend each line with a provided string

	slugify ST-3 - Convert a string into a url slug

	uid ST-4 [length_param] - Generate a unique id containing random letters and digits

	togglecase ST-5 - Convert a string to to toggle casing

	reverse ST-6 - Reverse a string

"""

if num_args == 1 : # no args
	print(version_info)
else :

	if sys.argv[1] in help_keys :

		print(help_info)

	elif num_args >= 2 :

		# bullet-list ST-1
		if sys.argv[1] in bullet_list_keys :
			import bulletList
		
		# prepend-list ST-2
		elif sys.argv[1] in prepend_list_keys :
			import prependList
		
		# slugify ST-3
		elif sys.argv[1] in slugify_keys :
			import slugify
		
		# uid ST-4
		elif sys.argv[1] in uid_keys :
			from uid import *

			try :
				length = sys.argv[2]
			except :
				length = 8
			
			print(generateUID(length), end = '')
			
		
		# togglecase ST-5
		elif sys.argv[1] in togglecase_keys :
			import togglecase
		
		# reverse ST-6
		elif sys.argv[1] in reverse_keys :
			import reverse
