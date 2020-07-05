#!/bin/bash

##
#
# Tests togglecase feature. In general, since this is an entirely random, it's
# difficult to test ouput perfectly, so we just ensure that the uid generated
# matches the length specified
#
##

status=0

echo "Testing: uid"
if [[ "$(python3 st.py uid 5 | wc -m)" -eq 5 ]]; then
	echo "Pass 1 of 1: Generated uid matches length given"
	status=0
else
	echo "Fail"
	status=1
fi


exit $status