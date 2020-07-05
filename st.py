import sys


num_args = len(sys.argv)

# options lists
help_keys = ["--help", "-h", "help"]
bullet_list_keys = ["bullet-list", "ST-1"]
prepend_list_keys = ["prepend-list", "ST-2"]
slugify_keys = ["slugify", "ST-3"]
togglecase_keys = ["togglecase", "memecase", "spongebob", "mock", "ST-5"]


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
		
		# togglecase ST-5
		elif sys.argv[1] in togglecase_keys :
			import togglecase
