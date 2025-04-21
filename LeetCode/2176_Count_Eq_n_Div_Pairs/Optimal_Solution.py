# Source: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/solutions/6658286/o-n-o-n-k-o-n-log-n-example-walkthrough-c-python-java/?envType=daily-question&envId=2025-04-17
from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def countPairs(self, nums: List[int], k:int) -> int:
        res = 0

        val_to_idxs = defaultdict(list)
        for idx, num in enumerate(nums):
            val_to_idxs[num].append(idx)

        divisors = []
        for d in range(1, int(k**(.5))+1):
            if k % d == 0:
                divisors.append(d)
                if d != k // d:
                    divisors.append(k//d)

        for idx_vector in val_to_idxs.values():
            idx_fmap = defaultdict(int)
            for i in idx_vector:
                gcdd = gcd(i, k)
                need = k//gcdd
                res += idx_fmap[need]
                for d in divisors:
                    if i % d == 0:
                        idx_fmap[d] += 1

        return res
    
"""
Second Approach: Mapping divisors

Time: O(n*sqrt(k))
Space: O(n)
"""