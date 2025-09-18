"""
217. Contains Duplicate
Level: Easy
Topics: Array, Hash Table, Sorting
Link: https://leetcode.com/problems/contains-duplicate
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set()
        for n in nums:
            if n in numSet:
                return True 
            numSet.add(n)
        return False