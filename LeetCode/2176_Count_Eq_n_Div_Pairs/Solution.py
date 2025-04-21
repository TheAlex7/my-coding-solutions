from typing import List
from collections import defaultdict
from math import gcd
# Intuitive approach
class Brute_Force_Solution():
    def addFact(self,n):
        return (n*(n+1))//2
    
    def countPairs(self, nums: List[int], k:int) -> int:
        res = 0
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if i * j % k == 0 and nums[i] == nums[j]:
                    res += 1
        return res

# Mapping Approach
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
First Approach: Brute Force using 2 pointers.

Time: O(n^2) operations to find all valid pairs
Space: O(1) only fixed auxiliary variables are used

Second Approach: Mapping divisors

Time: O(n*sqrt(k))
Space: O(n)

"""