from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
                

"""
Approach: Brute Force

Manually check every pair of values in array using only constant space.

Time: O(n^2)
Space: O(1)
"""