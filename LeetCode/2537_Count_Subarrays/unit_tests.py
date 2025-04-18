from Solution import Solution

if __name__ == "__main__":
    sol = Solution()
    # args = sys.argv[1:]
    # if len(args) != 2:
    #     print("Invalid arguments.")
    #     sys.exit()
    input_path = "cases.txt"

    with open(input_path, "r") as infile:
        inputs = [line.strip() for line in infile.readlines()]

    for i in range(len(inputs)):
        nums,k,expected = inputs[i].split("#")
        nums = [int(num) for num in nums.split(",")]   # cast everthing to integers
        k = int(k)

        ans = sol.countGood(nums, k)
        print(f"Your Answer: {ans} Expected: {expected}\n")
