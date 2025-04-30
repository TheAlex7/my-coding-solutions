# Automation Script to make new boiler plate folders with common format of LeetCode env challenges
import sys
import os

if __name__ == "__main__":
    args = sys.argv[1:] # retrieve command args that aren't the script 
    if len(args) != 1:
        print("Invalid input. Provide name of Coding challenge only. Delimited with \"_\"")
        sys.exit()

    name_of_challenge = args[0]
    os.makedirs(name_of_challenge, exist_ok=True) # create folder if doesn't exist
    with open(f"./{name_of_challenge}/cases.txt", "w") as file:
        file.write("# Enter Test Cases Here. hashtag delimiter. Line 1 is ignored. format: inputs#expected\n")

    with open(f"./{name_of_challenge}/DESC.md", "w") as file:
        name_arr = name_of_challenge.split("_")
        name_arr[0] += "."
        file.write(f"# {" ".join(name_arr)}\n\n[Source](```enter source link here```)\n\nDifficulty: \n\nBrief Description:\n")

    with open(f"./{name_of_challenge}/Solution.py", "w") as file:
        file.write("class Solution:\n\tdef func(self,inputs):\n\t\t\n\t\tpass")

    with open(f"./{name_of_challenge}/Optimal_Solution.py", "w") as file:
        file.write("class Solution:\n\tdef func(self,inputs):\n\t\t\n\t\tpass")

    with open(f"./{name_of_challenge}/unit_tests.py", "w") as file:
        file.write("from Solution import Solution\n\nif __name__ == \"__main__\":\n\tinput_path = \"cases.txt\"\n\n\twith open(input_path, \"r\") as infile:\n\t\t# load inputs while omitting first line in test case file\n\t\tinputs = [line.strip() for line in infile.readlines()][1:]\n\n\tfor i, (inputs,expected_output) in enumerate([tup.split(\"#\") for tup in inputs]):\n\t\t# process inputs further if necessary\n\n\t\t# rename func() to appropriate function name, if needed\n\t\tans = Solution().func(inputs)\n\t\tif str(ans) == expected_output:\n\t\t\tpassed = \"PASSED\"\n\t\telse:\n\t\t\tpassed = \"FAILED\"\n\t\tprint(f\"{i+1}) {passed} | Your Answer: {ans} | Expected: {expected_output}\\n\")")