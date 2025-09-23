"""
165. Compare Version Numbers
Level: Medium
Topics: Two Pointers, String
Link: https://leetcode.com/problems/compare-version-numbers?envType=daily-question&envId=2025-09-23
Time Complexity: O(n + m)
Space Complexity: O(1)
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n, m = len(v1), len(v2)
        i, j = 0, 0
        while i < n and j < m:
            num1 = int(v1[i])
            num2 = int(v2[j])
            if num1 > num2:
                return 1 
            elif num1 < num2:
                return - 1
            i += 1
            j += 1
        while i < n:
            num = int(v1[i])
            if num > 0:
                return 1
            i += 1
        while j < m:
            num = int(v2[j])
            if num > 0:
                return - 1
            j += 1
        return 0 
