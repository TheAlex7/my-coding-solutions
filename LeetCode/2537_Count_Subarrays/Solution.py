from typing import List

class Solution:    
    def countGood(self, nums: List[int], k: int) -> int:
        result = 0
        num_pairs = 0
        window = dict()
        i = j = 0    # left and right indexes
        last_moved = "j" # flag to keep track of which index to move
        while i<=j and j < len(nums):
            if last_moved == "j":
                if nums[j] in window:
                    window[nums[j]] += 1
                    quantity_j = window[nums[j]]
                    if quantity_j > 1:
                        num_pairs += quantity_j-1
                else:
                    window[nums[j]] = 1

            if num_pairs >= k:
                result += len(nums) - j

                quantity_i = window[nums[i]]
                if quantity_i > 0:
                    num_pairs -= quantity_i-1
                
                window[nums[i]] -= 1
                
                i += 1
                last_moved = "i"

            else:
                j += 1
                last_moved = "j"

        return result
            
"""
Approach: 2 pointers Sliding Window

This ended up being the solution given by the Leetcode Editorial for the challenge.
My code is not as condense since I tried using only one while loop

When submitting my code vs LeetCode's solution, my code is slightly faster for whatever reason.
Both solutions have the same Time/Space complexities nevertheless.

Time: O(n)
Space: O(n)

"""