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
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

nums = [1,2,3,1]