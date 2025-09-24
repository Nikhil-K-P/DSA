"""
15. 3Sum
Level: Medium
Topic: Two Pointers, Array, Sorting
Link: 
Time Complexity: O(n^2) 
Space Complexity: O(1)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        m = len(nums)
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, m - 1
            while l < r:
                Sum = nums[l] + nums[r] + n
                if Sum > 0:
                    r -= 1
                elif Sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
        return res