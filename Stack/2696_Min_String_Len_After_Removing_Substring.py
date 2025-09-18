"""
2696. Minimum String Length After Removing Substrings
Level: Easy
Topics: String, Stack
Link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings?envType=problem-list-v2&envId=stack
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        pair = {'B' : 'A', "D" : "C"}
        for c in s:
            if c in {'B', 'D'}:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack)