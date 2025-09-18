"""
242. Valid Anagram
Level: Easy
Topics: Hash Table, Sorting
Link: https://leetcode.com/problems/valid-anagram
Time Complexity: O(n)
Space Complexity: O(1) (since s and t consist of only lowercase English letters)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        return sMap == tMap