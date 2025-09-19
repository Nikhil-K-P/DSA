"""
155. Min Stack
Level: Medium 
Topics: Stack, Design
Link: https://leetcode.com/problems/min-stack?envType=problem-list-v2&envId=stack
Time Complexity: O(1) for each operation
Space Complexity: O(n) for stack and minStack
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()