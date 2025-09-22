"""
459. Repeated Substring Pattern
Level: Easy
Topics: String
Link: https://leetcode.com/problems/repeated-substring-pattern?envType=problem-list-v2&envId=string
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        newS = s + s
        return s in newS[1: -1]