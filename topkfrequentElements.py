# Given an integer array nums and an integer k, return the k most
# frequent elements, you may return answer in any order

# Example 1
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2 # in this case return the 2 most frequent
# Output: [1, 2]

# Solution using "bucket sort"
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty dictionary to count the frequency of each integer
        count = {}
        
        # Initialize a list of empty lists to group integers by frequency
        freq = [[] for i in range(len(nums)+1)]
        
        # Iterate through the input list and update the frequency count for each integer
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Iterate through the count dictionary and group integers by frequency in the freq list
        for n, c in count.items():
            freq[c].append(n)
        
        # Initialize an empty list to hold the top k frequent integers
        res = []
        
        # Iterate through the freq list backwards and add integers to res until its length is k
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
# O(n) time complexity
