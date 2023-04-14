# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all elements of nums except nums[i].

# The product of any prefix or suffic of nums is "guaranteed" to fit in a 32 bit int

# You must write an algorithm that runs in O(n) time andd without using the division operation

# Example 1
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefit *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res
    
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)