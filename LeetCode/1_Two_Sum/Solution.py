from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []
    
"""
Approach: Hashing

Considering a python sets are created using a HashTable, look up time in the visited set should be constant.
As every integer (n) in the nums list is visited, the set will grow to be at most n elements in size.

Time: O(n)
Space: O(n)
"""