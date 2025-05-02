from Solution import Solution

if __name__ == "__main__":
	input_path = "cases.txt"

	with open(input_path, "r") as infile:
		# load inputs while omitting first line in test case file
		inputs = [line.strip() for line in infile.readlines()][1:]

	for i, (calls,args,expected_output) in enumerate([tup.split("#") for tup in inputs]):
		calls = [s.strip() for s in calls.replace("\"","").split(",")]
		args = args.replace("\"","").split(".")
		tups = []
		for s in args:
			s.replace("[", "")
			s.replace("]", "")
			temp_ls = []
			for arg in s.split(","):
				temp_ls.append(arg.strip())
			tups.append(tuple(temp_ls))
		expected_output = [out.strip() for out in expected_output.replace("\"","").split(",")]

		test_obj = Solution()
		ans = []
		for i, call in enumerate(calls):
			tup_args = tups[i]
			out = "null"
			if call == "TimeMap":
				test_obj = Solution()
			elif call == "set":
				test_obj.set(tup_args[0],tup_args[1],tup_args[2])
				out = "null"
			elif call == "get":
				out = test_obj.get(tup_args[0],tup_args[1])
			ans.append(out)

		if ans == expected_output:
			passed = "PASSED"
		else:
			passed = "FAILED"
		print(f"{i+1}) {passed} | Your Answer: {ans} | Expected: {expected_output}\n")