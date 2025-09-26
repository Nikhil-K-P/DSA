"""
153. Find Minimum in Rotated Sorted Array
Level: Medium
Topics: Array, Binary Search
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Time Complexion: O(log n)
Space Complexion: O(1)
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res