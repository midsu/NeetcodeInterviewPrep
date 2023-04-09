# two sum

# EXAMPLE 1

# nums = [1,3,5,2], target = 4
# 1 and 3 equals to target 4

# solution using hash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
