from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret = []
        gain = 0
        for i, val in enumerate(nums):
            if val == key:
                for j in range(max(i-k,gain), min(i+k,len(nums)-1)+1): 
                    ret.append(j)
                    gain = j + 1

        return ret
    
"""
Approach: Single pass with pointer

While iterating, maintain a pointer to track last added index to avoid adding duplicates to return array

Time: O(n) one pass
Space: O(n) size of returning array can be at most the size of input arr 
"""