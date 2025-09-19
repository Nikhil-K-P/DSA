"""
150. Evaluate Reverse Polish Notation
Level: Medium
Topics: Array, Math, Stack
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation?envType=problem-list-v2&envId=stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(t))
        return stack[-1]