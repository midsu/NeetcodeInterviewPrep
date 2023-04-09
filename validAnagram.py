# Given two strings s and t, return true 'if' t is an anagram of s, and false otherwise

# EXAMPLE 1
# Input: s = "anagram", t = "nagaram"
# Output: true

# EXAMPLE 2
# Input: s = "rat", t = "car"
# Output: false

# SOLUTION 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

# SOLUTION 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


# SOLUTION 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)

        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True



