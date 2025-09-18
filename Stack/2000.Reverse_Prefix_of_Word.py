"""
2000. Reverse Prefix of Word
Level: Easy
Topics: String, Stack
Link: https://leetcode.com/problems/reverse-prefix-of-word?envType=problem-list-v2&envId=stack
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        pos = -1
        for idx, c in enumerate(word):
            stack.append(c)
            if c == ch:
                pos = idx
                break 
        res = ""
        for i in range(len(word)):
            if i <= pos:
                res += stack.pop()
            else:
                res += word[i]
        return res