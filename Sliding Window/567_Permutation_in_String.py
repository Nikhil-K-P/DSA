"""
567. Permutation in String
Level: Medium
Topic: Hash Table, Two Pointers, String, Sliding Window
Link: https://leetcode.com/problems/permutation-in-string
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        s2Count = [0] * 26
        n, m = len(s1), len(s2)
        if m < n:
            return False
        for i in range(n):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        left = 0
        for right in range(n, m):
            if s1Count == s2Count:
                return True 
            s2Count[ord(s2[left]) - ord('a')] -= 1
            s2Count[ord(s2[right]) - ord('a')] += 1
            left += 1
        if s1Count == s2Count:
            return True 
        return False