def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            res = ""
            count = 0
            digit = "0"
            for num in result:
                if num != digit :
                    if count > 0:
                        res += f"{count}{digit}"
                    digit = num
                    count = 0
                count += 1
            res += f"{count}{digit}"  # last digit
            result = res
        return result

"""
Approach: Intuition (Iterative)

"""