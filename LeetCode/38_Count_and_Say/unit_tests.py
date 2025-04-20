from Solution import Solution

if __name__ == "__main__":
    sol = Solution()
    input_path = "cases.txt"

    with open(input_path, "r") as infile:
        inputs = [line.strip() for line in infile.readlines()]

    for i, (inp,expected) in enumerate([tup.split("#") for tup in inputs]):
        inp = int(inp)
        ans = sol.countAndSay(inp)
        if ans == expected:
            passed = "PASSED"
        else:
            passed = "FAILED"
        print(f"{i+1}) {passed} Your Answer: \"{ans}\" Expected: \"{expected}\"\n")
