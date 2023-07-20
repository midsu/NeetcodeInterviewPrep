'''
Given a string s containing just the characters '(', ')', '{', '}', '[',  and ']'
determine if the input string is valid

An input string is valid if:
    1- Open brackets must be closed by the same type of brackets
    2- Open brackets must be close in the correct order

example:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to store opening brackets
        # Dictionary to store the mapping of closing brackets to opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"} 

        for c in s:  # Iterate through each character in the input string 's'
            if c in closeToOpen:  # Check if the character is a closing bracket
                if stack and stack[-1] == closeToOpen[c]:  # If the stack is not empty and the top element matches the corresponding opening bracket
                    stack.pop()  # Pop the top element from the stack (matching opening bracket found)
                else:
                    return False  # If the stack is empty or the top element doesn't match the corresponding opening bracket, the string is invalid
            else:
                stack.append(c)  # If the character is an opening bracket, add it to the stack

        return True if not stack else False  # If the stack is empty after processing all characters, the string is valid; otherwise, it is invalid
