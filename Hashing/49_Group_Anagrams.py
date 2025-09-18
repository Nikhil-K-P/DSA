"""
49. Group Anagrams
Level: Medium
Topics: Hash Table, String, Sorting
Link: https://leetcode.com/problems/group-anagrams
Time Complexity: O(n * m) where n - number of strings and m - length of a string
Space Complexity: O(n * m)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            anagrams[tuple(counter)].append(s)
        return list(anagrams.values())