"""
1221. Split a String in Balanced Strings
Level: Easy
Topics: String, Greedy, Counting
Link: https://leetcode.com/problems/split-a-string-in-balanced-strings?envType=problem-list-v2&envId=counting
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countR = 0
        res = 0
        for c in s:
            if c == "R":
                countR += 1
            else:
                countR -= 1
            if countR == 0:
                res += 1
        return res