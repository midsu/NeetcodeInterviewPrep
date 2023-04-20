# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero

# Note:
# The solution set must not contain duplicate triplets

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4]
# Solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]   
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a +