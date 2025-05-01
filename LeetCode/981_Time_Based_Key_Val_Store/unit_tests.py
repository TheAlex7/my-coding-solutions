from Solution import Solution

if __name__ == "__main__":
	input_path = "cases.txt"

	with open(input_path, "r") as infile:
		# load inputs while omitting first line in test case file
		inputs = [line.strip() for line in infile.readlines()][1:]

	for i, (inputs,expected_output) in enumerate([tup.split("#") for tup in inputs]):
		# process inputs further if necessary

		# rename func() to appropriate function name, if needed
		ans = Solution().func(inputs)
		if str(ans) == expected_output:
			passed = "PASSED"
		else:
			passed = "FAILED"
		print(f"{i+1}) {passed} | Your Answer: {ans} | Expected: {expected_output}\n")