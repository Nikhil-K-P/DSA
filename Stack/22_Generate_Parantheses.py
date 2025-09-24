"""
22. Generate Parentheses
Level: Medium
Topic: Stack, Backtracking, Dynamc Programming
Link: https://leetcode.com/problems/generate-parentheses
Time Complexity: O(4^n / sqrt(n))   
Space Complexity: O(n)   
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []
        def dfs(nOpen, nClose):
            if nOpen == nClose == n:
                res.append(''.join(stack))
                return 
            if nOpen < n:
                stack.append('(')
                dfs(nOpen + 1, nClose)
                stack.pop()
            if nClose < nOpen and nClose < n:
                stack.append(')')
                dfs(nOpen, nClose + 1)
                stack.pop()
        dfs(0, 0)
        return res