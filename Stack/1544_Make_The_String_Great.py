"""
1544. Make The String Great
Level: Easy
Topics: Stack, String
Link: https://leetcode.com/problems/make-the-string-great?envType=problem-list-v2&envId=stack
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def swapcase(self, s: str) -> str:
        if ord(s) >= 65 and ord(s) <= 90:
            return s.lower()
        return s.upper()

    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            newC = self.swapcase(c)
            if stack and stack[-1] == newC:
                stack.pop()
                continue 
            stack.append(c)
        return ''.join(stack)