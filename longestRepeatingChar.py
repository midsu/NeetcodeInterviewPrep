'''
You are given a string s and an integer k.You can choose any character ofthe strig and
changeittoany other uppercase English character. You can perform this opertion at most
k times.

Return the length of the longest substring containting 
the same letter you can get after oerforming the above operation.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            res = 0

            l = 0
            for r in range(len(s)):
                count[s[r]] = 1 + count.get[s[r], 0]

                while (r - l + 1) - max(count.values()) > k:
                    count[s[l]] -= 1
                    l += 1

                res = max(res, r - l + 1)
            return res