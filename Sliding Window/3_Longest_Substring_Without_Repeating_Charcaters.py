"""
3. Longest Substring Without Repeating Characters
Level: Medium
Topics: Hash Table, String, Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
Time Complexity: O(n)
Space Complexity: O(n) 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j = 0, 0
        cSet = set()
        res = 0
        while j < n:
            while i < len(s) and s[j] in cSet:
                cSet.remove(s[i])
                i += 1
            cSet.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res 