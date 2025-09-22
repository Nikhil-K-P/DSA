"""
20. Valid Parentheses
Level: Easy
Topics: Stack, String
Link: https://leetcode.com/problems/valid-parentheses
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {"]" : "[", ")" : "(", "}" : "{"}
        for c in s:
            if c in bracketMap:
                if not stack or bracketMap[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True