"""
287. Find the Duplicate Number
Level: Medium
Topics: Array, Two Pointers, Binary Search, Linked List, Bit Manupulation
Link: https://leetcode.com/problems/find-the-duplicate-number
Time Complexion: O(n)
Space Complexion: O(1)
"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        slow2 = 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow