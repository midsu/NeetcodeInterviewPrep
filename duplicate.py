# Given an integer value num, rerurn true if any value appears 'at least twice' in
# the array, and return false if every element is distinct.

# EXAMPLE 1
# input: num = [1,2,3,1]
# Output: true

# EXAMPLE 2
# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def containDuplicate(self, nums: list[int]) -> bool:
        # Initialize an empty set to keep track of unique integers
        hashset = set()

        # Iterate through the input list
        for n in nums:
            # If the integer is already in the hashset, then there's a duplicate
            if n in hashset:
                return True
            # Otherwise, add the integer to the hashset
            hashset.add(n)
        
        # If we've iterated through the entire list without finding a duplicate, then return False
        return False
    
    
nums = [1,2,3,1]
