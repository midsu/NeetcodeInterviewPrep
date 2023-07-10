'''
Finding the longest consecutive sequence in a list of number and returning its length
Time complexity of O(n) and space complexity of O(n)
'''

class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

sequence = [100, 4, 200, 1, 3, 2]
solution = Solution()
print(solution.longest_consecutive(sequence))

'''
input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: [1,2,3,4] therefore longest cons sequence is 4
'''