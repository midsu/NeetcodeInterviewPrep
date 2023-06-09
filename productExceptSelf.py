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
        # Initialize a result list with all elements set to 1
        res = [1] * (len(nums))

        # Calculate the prefix products
        prefix = 1
        for i in range(len(nums)):
            # Store the prefix product of all elements before the current element
            res[i] = prefix
            prefix *= nums[i]
        
        # Calculate the postfix products
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the postfix product of all elements after the current element
            res[i] *= postfix 
            postfix *= nums[i]
        
        # Return the resulting list
        return res
    
    
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)
