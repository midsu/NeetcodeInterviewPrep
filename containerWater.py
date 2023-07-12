'''
Given n non-negative intergers where eah represent a point of coordinate (i, a1) . 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
find two lines, which together with x-axis, forms a container constains the most water.

Input: height [1, 8, 6, 2, 5, 4, 8, 3, 7] 
Output: 49
Explaination; the vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7], 
In this case the max area of water(blue section), the container can contain is 49.

'''

class solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # Calculate the area between the lines at indices l and r
            area = (r - l) * min(height[l], height[r])
            # Update the maximum area if the calculated area is greater
            res = max(area, res)

            # Move the index l or r towards the center based on which line is shorter
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
