'''
You are given a string s and an integer k.You can choose any character ofthe strig and
changeittoany other uppercase English character. You can perform this opertion at most
k times.

Return the length of the longest substring containting 
the same letter you can get after oerforming the above operation.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store the frequency count of characters in the current window
        res = 0     # Variable to store the maximum length of the substring with the same characters

        l = 0       # Left pointer of the sliding window
        for r in range(len(s)):  # Right pointer of the sliding window (expands the window to the right)
            # Update the count of the character at the right pointer and handle its initial count as 0
            count[s[r]] = 1 + count.get(s[r], 0)
            # Check if the number of characters to be replaced (total characters in window - max character count) exceeds 'k'
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1  # Reduce the count of the character at the left pointer
                l += 1            # Move the left pointer to the right to shrink the window
            # Update the result with the maximum length of the substring with the same characters
            res = max(res, r - l + 1) # r - l + 1 is the size of the window/substring

        return res
