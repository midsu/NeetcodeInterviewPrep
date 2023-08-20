'''
Greedy Algorithm Problem

Given an array of N integers, Find the highest product by multiplying 3 elements

Input: [1, 2, 3, 4]
Output: 2 * 3 * 4 = 24

'''

class Solution:
    # @param A: list of integers
    # return an integer
    def max3(self, A):
        A = sorted(A)

        hi3 = A[-1] * A[-2] * A[-3]
        lo2hi1 = A[0] * A[1] * A[-1]

        return max(hi3, lo2hi1)

numbers = [1, 2, 3, 4]
res = Solution()

output = res.max3(numbers)
print(output)