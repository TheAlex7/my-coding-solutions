class Solution:
    def runLengthEncoding(self, n: str) -> str:
        res = ""
        count = 0
        digit = -1
        for c in n:
            num = int(c)
            if num != digit :
                if count > 0:
                    res += f"{count}{digit}"
                digit = num
                count = 0
            count += 1
        res += f"{count}{digit}"  # last digit
        return res
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.runLengthEncoding(self.countAndSay(n-1))

"""
Approach: Intuition

Same concept as optimal but not written as cleanly.

Time: O(2^n)
Operations increase exponentially as the output of Encoding may be double the input.

Space: O(2^n)
Inputs/Outputs are strings which also increase exponentially in size.
"""