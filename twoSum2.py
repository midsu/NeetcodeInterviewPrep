# Given an array integers that is already "sorted in ascending order". 
# Find two numbers such that they add up to a specific target number. 
# The function twoSum should return indices of the two numbers 
# such that they add up to the target, where index1 must be less than index2.

# NOTE:
# Your returned answers (both inddex1 and index2) are not zero-based
# You may assume that each input would have exactly one solution
# and you may not use the same element twice.

# EXAMPLE:


# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1,2]
# Exmplanation: (index here started from 1, not 0). The sum of 2 and 7 is 9,
# therefore index1 = 1, index2 = 2 
    
# Import the necessary modules
from typing import List

class Solution:
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # Initialize two variables l and r to track the indices of the two numbers
    # in the numbers list that add up to the target
    l, r = 0, len(numbers) - 1

    # Loop through the list until the two numbers that add up to the target are found
    while l < r:
        # Calculate the sum of the two numbers at indices l and r
        curSum = numbers[l] + numbers[r]

        # If the current sum is greater than the target, decrement r to move to a smaller number
        if curSum > target:
            r -= 1
        # If the current sum is less than the target, increment l to move to a larger number
        elif curSum < target:
            l += 1
        # If the current sum is equal to the target, return the indices of the two numbers as a list
        else:
            return [l + 1, r + 1]

    # If no two numbers that add up to the target are found, return an empty list
    return []
    
    
# Create an instance of the Solution class
s = Solution()

# Define a list of numbers and a target
numbers = [2, 7, 11, 15]
target = 9

# Call the twoSum method with the list of numbers and target
result = s.twoSum(numbers, target)

# Print the result
print(result)
