#!/bin/bash

status=0

echo "Testing: reverse"

input="green eggs and ham"
expected="mah dna sgge neerg"

if [[ `echo $input | python3 st.py reverse` == "$expected" ]]; then
	echo "Pass 1 of 2: Line reversed successfully"
	status=0
else
	echo "Fail 1 of 2: Line reverse failed"
	status=1
fi

read -r -d '' input2 << EOD
1
2
3
EOD

read -r -d '' expected2 << EOD
3
2
1
EOD

if [[ `echo "$input" | python3 st.py reverse` == "$expected" ]]; then
	echo "Pass 2 of 2: Multiline reversed successfully"
	status=0
else
	echo "Fail 2 of 2: Multiline reverse failed"
	status=1
fi

exit "$status"