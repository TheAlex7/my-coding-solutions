from Solution import Solution

if __name__ == "__main__":
	input_path = "cases.txt"

	with open(input_path, "r") as infile:
		# load inputs while omitting first line in test case file
		inputs = [line.strip() for line in infile.readlines()][1:]

	for i, (inputs,expected_output) in enumerate([tup.split("#") for tup in inputs]):
		# process inputs further if necessary
		ls = [int(elem) for elem in inputs.split(",")]
		kdist = ls.pop()
		key = ls.pop()
		
		expected = [int(elem) for elem in expected_output.split(",")]

		# rename func() to appropriate function name, if needed
		ans = Solution().findKDistantIndices(ls,key,kdist)
		if ans == expected:
			passed = "PASSED"
		else:
			passed = "FAILED"
		print(f"{i+1}) {passed} | Your Answer: {ans} | Expected: {expected}\n")