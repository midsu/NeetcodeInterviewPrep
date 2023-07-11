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
        res = []  # Initialize a list to store the resulting triplets
        nums.sort()  # Sort the input array in ascending order

        for i, a in enumerate(nums):  # Iterate over the elements of the sorted array
            if i > 0 and a == nums[i - 1]:  # Skip duplicate elements to avoid duplicate triplets
                continue

            l, r = i + 1, len(nums) - 1  # Initialize two pointers: l points to the element after a, r points to the last element

            while l < r:  # Loop until the two pointers meet
                threeSum = a + nums[l] + nums[r]  # Calculate the sum of the three elements

                if threeSum > 0:  # If the sum is greater than 0, decrement r to get a smaller element
                    r -= 1
                elif threeSum < 0:  # If the sum is less than 0, increment l to get a larger element
                    l += 1
                else:  # If the sum is 0, a valid triplet is found
                    res.append([a, nums[l], nums[r]])  # Add the triplet to the result list
                    l += 1  # Increment l to move to the next unique element

                    while nums[l] == nums[l - 1] and l < r:  # Skip duplicate elements to avoid duplicate triplets
                        l += 1
        return res  # Return the list of unique triplets that sum up to zero

# example
