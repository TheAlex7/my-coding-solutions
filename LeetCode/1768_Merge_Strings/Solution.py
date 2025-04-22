class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		result = []
		i = j = 0
		alt = -1 # flag to delegate the alternating
		while i < len(word1) and j < len(word2): # will run for as long as the shorter string
			if alt < 0:
				result.append(word1[i])
				i += 1
			else:
				result.append(word2[j])
				j += 1

			alt *= -1 # alternate pointer

		# append rest of remaing letters
		if i < len(word1): # 1st word was longer
			result.append(word1[i:])
		if j < len(word2): # 2nd word was longer
			result.append(word2[j:])

		return "".join(result) # string builder to avoid creating intermediate strings that weigh on memory
	
"""
Approach: 2 Pointers

Each character from both words are visited until the end of the shorter string is reached. Then the remaining of the last string is appended to the result list.

Time: O(n) where n is the length of the shorter string. 
Space: O(n + m) result variable will be the size of input

"""