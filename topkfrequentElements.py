# Given an integer array nums and an integer k, return the k most
# frequent elements, you may return answer in any order

# Example 1
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2 # in this case return the 2 most frequent
# Output: [1, 2]

# Solution using "bucket sort"
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

# O(n) time complexity

