#!/bin/bash

##
#
# Tests togglecase feature. In general, since this is an entirely random, it's
# difficult to test ouput perfectly, so we just ensure that the original line
# is the same length and has changed
#
##

status=0

# oneline
oneline=$(cat tests/oneline.txt)
afterOneline=$(python3 st.py togglecase < tests/oneline.txt)

onelineCount=$(echo $oneline | wc -m)
afterOnelineCount=$(echo $afterOneline | wc -m)

if [[ "$oneline" == "$afterOneline" ]]; then
	echo "Fail: Original oneline string has not been altered"
	status=1
else
	echo "Pass 1 of 4: Oneline string does not match original string"

	if [[ $onelineCount -eq $afterOnelineCount ]]; then
		echo "Pass 2 of 4: Oneline string length has not changed"
		status=0
	else
		echo "Fail: Altered oneline string length has changed"
		status=1
	fi

fi

# multiline
multiline=$(cat tests/multiline.txt)
afterMultiline=$(python3 st.py togglecase < tests/multiline.txt)

multilineCount=$(echo $multiline | wc -m | xargs)
afterMultilineCount=$(echo $afterMultiline | wc -m | xargs)

if [[ "$multiline" == "$afterMultiline" ]]; then
	echo "Fail: Original multiline string has not been altered"
	status=1
else
	echo "Pass 3 of 4: Multiline string does not match original string"

	if [[ "$multilineCount" -eq "$afterMultilineCount" ]]; then
		echo "Pass 4 of 4: Multiline string length has not changed"
		status=0
	else
		echo "Fail: Altered multiline string length has changed"
		status=1
	fi

fi

exit $status