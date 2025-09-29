"""
976. Largest Perimeter Triangle
Level: Easy
Topics: Array, Greedy, Sorting
Link: https://leetcode.com/problems/largest-perimeter-triangle?envType=problem-list-v2&envId=sorting
Time Complexity: O(n * logn)
Space Complexity: O(1)
"""


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort(reverse=True)
        for i in range(n - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if b + c > a:
                res = a + b + c 
                break 
        return res 