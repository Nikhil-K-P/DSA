"""
1662. Check if Two String Arrays are Equivalent
Level: Easy
Topics: Array, String
Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent?envType=problem-list-v2&envId=string
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)