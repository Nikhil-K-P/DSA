"""
901. Online Stock Span
Level: Medium
Topic: Stack, Design, Monotonic Stack
Link: 
Time Complexity: O(n) 
Space Complexity: O(n)
"""


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
