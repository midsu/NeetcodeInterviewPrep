'''
Given an array A of a random permutation of numbers from 1 to N, 
Given B the number of swaps in A that we can make,

Find the "Largest" permutation that we can make.

Input: A = [1, 3, 2], B = 1
Output: [3, 1 ,2] -> swap 1 and 3

Input: A = [1, 2, 3, 4], B = 1
Output: [4, 2, 3 , 1] -> swap 1 and 4

Input: A = [3, 2, 4, 1, 5], B = 3
       (1) [5, 2, 4, 1, 3]          swap 5 and 3, 
       (2) [5, 4, 2, 1, 3]          swap 4 and 2, 
       (3) [5, 4, 3, 1, 2]          swap 3 and 2
Output: [5, 4, 3, 1, 2]

Greedily replace the higher element
N -> N-1 -> ....

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        _max = len(A)
        d = {x: i for i, x in enumerate(A)}  # Create a dictionary to store element-to-index mapping

        while B and i < len(A):
            j = d[_max]  # Get the index of the current maximum element
            if i == j:
                pass  # No need to swap if the current element is already at its correct position
            else:
                B -= 1  # Decrement the number of swaps available
                A[i], A[j] = A[j], A[i]  # Swap the elements at indices i and j
                d[A[i]], d[A[j]] = d[A[j]], d[A[i]]  # Update the dictionary with new indices

            i += 1
            _max -= 1  # Decrement the value of the _max variable

        return A

intervals = [3, 2, 4, 1, 5]
solution = Solution()
result = solution.solve(intervals, 3)  # Call the solve method with the given list and B = 3
print(result)  # Print the modified list after performing the swaps
