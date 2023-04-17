# Given a string s, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases

# EXAMPLE 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Explanation: "amanaplanacanalpanama" is a palindrome

# EXAMPLE 2:

# Input: s = "race a car"
# Output: False
# Explanation: "raceacar" is not a palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# OR
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > 1 and not self.alphaNum(s[r]):
                r -= l
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1, r - 1
        return True

def alphanum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))