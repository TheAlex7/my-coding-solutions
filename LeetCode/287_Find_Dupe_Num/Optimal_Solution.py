from typing import List

class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		# Floyd's tortoise and hare algorithm
		fast = nums[0]
		slow = nums[0]
		while True:
			fast = nums[nums[fast]]
			slow = nums[slow]
			if fast == slow:
				break
			
		slow2 = nums[0]
		while slow2 != slow:
			slow2 = nums[slow2]
			slow = nums[slow]
			
		return slow
	
"""
Approach: LinkedList loop detection with Floyd's algorithm

Start of loop is always the duplicate value

Time: O(n)
Space: O(1)
"""