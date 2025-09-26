"""
33. Search in Rotated Sorted Array
Level: Medium
Topics: Array, Binary Search
Link: https://leetcode.com/problems/search-in-rotated-sorted-array
Time Complexion: O(log n)
Space Complexion: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid 
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 
