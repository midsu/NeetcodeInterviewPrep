"""
Given an integer x, return true if x is a palindrome, and false otherwise

Input: x = 121
Output: True

Input: x = -121
Output = False  // -1 and 1
"""

class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        string_x = str(x)
        left_point = 0
        right_point = len(string_x)-1

        while(left_point < right_point):
            if not string_x[left_point] == string_x[right_point]:
                return False
            left_point += 1
            right_point -= 1

            return True
