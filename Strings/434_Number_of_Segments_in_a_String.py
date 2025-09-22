"""
434. Number of Segments in a String
Level: Easy
Topics: String
Link: https://leetcode.com/problems/number-of-segments-in-a-string?envType=problem-list-v2&envId=string
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def countSegments(self, s: str) -> int:
        word = ''
        s += ' '
        count = 0
        for c in s:
            if c == ' ':
                if word:
                    count += 1
                word = ''
                continue
            word += c
        return count