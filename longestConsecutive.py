# Given an unsorted array of integers, find the length of the longest consequtive elements sequence
# Your algorithm should run in O(n) comlexity

# EXAMPLE
# Input: [100, 4 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4], 
# therefore its length is 4


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list of integers into a set for fast lookup
        numSet = set(nums)
        
        # Initialize the longest sequence length to zero
        longest = 0

        # Loop through each number in the input list
        for n in nums:
            # Check if the number is the start of a sequence by checking if the previous number is not in the set
            if (n - 1) not in numSet:
                # If it is the start of a sequence, find the length of the sequence by incrementing the number until it is no longer in the set
                length = 0
                while (n + length) in numSet:
                    length += 1
                
                # Update the longest sequence length if the current sequence is longer
                longest = max(length, longest)
        
        # Return the length of the longest sequence found
        return longest

    # O(n) time complexity
    # O(n) space complexity 
