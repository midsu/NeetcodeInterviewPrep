# Given an array of strings str, group the anagrams together. 
# You can return answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a differnt 
# word or phrase, typically using all the origiran letters exactly once.
 
# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


# Solution using Hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[list[str]]:
        res = defaultdict(list) # mapping charCount to List of Anagram

        for s in strs:
            count = [0] * 26 # a ....z

            for c in s:
                count[ord(c) - ord("a")] +=1 
                # above line of code is cuz we want to map "a" to index 0, and map "z" to index 25,
                # so we take ascii val of current char (c) we are at and minus ascii val "a", 
                # same as doing this:
                # a = 80 -> 0, 80 - 80 = 0
                # b = 81 -> 1, 81 - 80 = 1

            res[tuple(count)].append(s)

        return res.values()

# O(m * n ) time complexity
