# Given an array of strings str, group the anagrams together. 
# You can return answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a differnt 
# word or phrase, typically using all the origiran letters exactly once.
 
# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


# Solution using Hashmap
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
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
'''
# O(m * n ) time complexity


''' Another Solution '''
# Solution using Hashmap
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a defaultdict to store anagrams
        anagram_map = defaultdict(list)
        result = []

        # Loop through the list of strings
        for s in strs:
            # Convert the string to a sorted tuple of characters
            sorted_s = tuple(sorted(s))
            # Append the original string to the corresponding anagram group
            anagram_map[sorted_s].append(s)

        # Loop through the groups of anagrams
        for value in anagram_map.values():
            # Append each group to the result list
            result.append(value)

        return result

# Test Cases
test_case_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test_case_2 = ["hello", "world", "goodbye"]
test_case_3 = ["listen", "silent", "elbow", "below", "state", "taste"]

# Create an instance of the Solution class
solution = Solution()

# Call the groupAnagrams function on each test case
output_1 = solution.groupAnagrams(test_case_1)
output_2 = solution.groupAnagrams(test_case_2)
output_3 = solution.groupAnagrams(test_case_3)

# Print the results
print("Test case 1: ",output_1)
print("Test case 2: ",output_2)
print("Test case 3: ",output_3)

