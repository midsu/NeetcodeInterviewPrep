'''
Given a list of intervals: 
[Start, End]

Find the length of maximal set of mutually disjoint interval.

Input: [[1, 2], [2, 10], [4, 6]]

Output: 2 -> [1, 2], [4, 6]

'''

class Solution:
    def interval(self, A):
        # sort the intervals by their endings
        A.sort(key = lambda x: x[1])

        # the first interval as [start, end] earliest 
        prev_s, prev_e = A[0]
        count = 1
        # given start and end of each interval in A, loop
        for s, e in A:
            # is the start of current interval before the end of previews interval? overlapping?
            if s <= prev_e:
                pass
            else:
                # not intersecrting with previews interval so increase count
                prev_s, prev_e = s, e 
                count += 1
        return count

# Test Case 1: Non-overlapping intervals
# Intervals are already sorted by end times.
intervals1 = [[1, 3], [4, 6], [7, 9], [10, 12]]
solution = Solution()
result1 = solution.interval(intervals1)
# Expected output: 4, as there are 4 non-overlapping intervals.
print(result1)
