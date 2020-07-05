#!/bin/bash

# run from root directory
# name all tests "test_[feature].sh"

tests=$(ls tests/test_*)

for test in $tests; do
	$test
done