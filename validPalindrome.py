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



# Define a class called Solution
class Solution:
    # Define a method called isPalindrome that takes a string s as input
    # and returns True if s is a palindrome, considering only alphanumeric
    # characters and ignoring cases
    def isPalindrome(self, s: str) -> bool:
        # Initialize an empty string called newStr
        newStr = ""
        # Iterate over each character c in the input string s
        for c in s:
            # If the character c is alphanumeric, convert it to lowercase and
            # append it to the new string newStr
            if c.isalnum():
                newStr += c.lower()
        # Return True if the new string newStr is equal to its reverse, which
        # means that the input string s is a palindrome
        return newStr == newStr[::-1]
# OR with o(n) for time complexity, and o(1) for space complexity
# Define another class called Solution
class Solution:
    # Define a method called isPalindrome that takes a string s as input
    # and returns True if s is a palindrome, considering only alphanumeric
    # characters and ignoring cases
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers l and r to the left and right ends of the input string s
        l, r = 0, len(s) - 1

        # Iterate over the string s by moving l to the right and r to the left
        # until they meet or cross each other
        while l < r:
            # If the character at index l is not alphanumeric, skip it
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # If the character at index r is not alphanumeric, skip it
            while r > 1 and not self.alphaNum(s[r]):
                r -= l
            # If the characters at indexes l and r are not equal after converting
            # them to lowercase, return False because s is not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            # Move l to the right and r to the left
            l , r = l + 1, r - 1
        # If the function has not returned False yet, s is a palindrome
        return True

    # Define another method called alphaNum that takes a character c as input
    # and returns True if c is alphanumeric and False otherwise
    def alphaNum(self, c):
        # Return True if the ASCII value of c is within the range of alphanumeric
        # characters (i.e., A-Z, a-z, or 0-9)
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
