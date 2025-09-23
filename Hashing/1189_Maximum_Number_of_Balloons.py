"""
1189. Maximum Number of Balloons
Level: Easy
Topics: Hashing, String, Counting
Link: https://leetcode.com/problems/maximum-number-of-balloons
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = len(text)
        frequency = {}
        for c in text:
            frequency[c] = 1 + frequency.get(c, 0)
        for c in "balon":
            count = frequency.get(c, 0)
            if c == "l" or c == "o":
                count = count // 2
            res = min(count, res)
            if count == 0:
                return 0
        return res