"""
844. Backspace String Compare
Level: Easy 
Topics: Stack, Two Pointers, String
Link: https://leetcode.com/problems/backspace-string-compare?envType=problem-list-v2&envId=stack
Time Complexity: O(N)
Space Complexity: O(N)
Follow up: Can you solve it in O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def text(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        return text(s) == text(t)