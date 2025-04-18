# source = https://leetcode.com/problems/count-the-number-of-good-subarrays/solutions/6642976/count-the-number-of-good-subarrays/?envType=daily-question&envId=2025-04-16

from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        for left in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
            if same >= k:
                ans += n - right
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
        return ans