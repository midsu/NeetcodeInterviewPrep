# Given an unsorted array of integers, find the length of the longest consequtive elements sequence
# Your algorithm should run in O(n) comlexity

# EXAMPLE
# Input: [100, 4 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4], 
# therefore its length is 4

class Solution:
    def longestConsecutive(sekf, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length+=1
                longest = max(length, longest)
        return longest