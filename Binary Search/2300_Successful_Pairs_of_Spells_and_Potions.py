"""
2300. Successful Pairs of Spells and Potions
Level: Medium
Topic: Array, Binary Search, Sorting
Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions?envType=daily-question&envId=2025-10-08
Time Complexity: O(n log m) where n is the length of spells and m is the length of potions
Space Complexity: O(1)
Good Question for Review - Yes
"""


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n = len(spells)
        m = len(potions)
        res = [0] * n
        potions.sort()
        for i, strength in enumerate(spells):
            l, r = 0, m - 1
            while l <= r:
                mid = l + (r - l) // 2
                if potions[mid] * strength >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            res[i] = m - l
        return res