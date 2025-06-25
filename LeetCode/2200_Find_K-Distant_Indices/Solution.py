from typing import List
class Solution:
	def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
		ranges = []
		ret = []
		for i, val in enumerate(nums):
			if val == key:
				ranges.append((max(i-k,0), min(i+k,len(nums)-1)))

		for idx in range(len(ranges)):
			low, high = ranges[idx]
			if idx < len(ranges)-1 and high >= ranges[idx+1][0]:
				terminate = ranges[idx+1][0]
			else:
				terminate = len(nums)
			for j in range(low,high+1):
				if j == terminate:
					break
				ret.append(j)

		return ret
	
	"""
Approach: Array and Range Traversal

Traverse array while adding to an auxiliary array which keeps track of all the possible ranges. 
Iterate through the auxiliary array while adding only unique values (early terminating when high 
boundary reaches the next range's low boundary)

Time: O(n)
Space: O(n) 
"""