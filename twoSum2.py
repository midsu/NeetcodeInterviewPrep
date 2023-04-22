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


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
