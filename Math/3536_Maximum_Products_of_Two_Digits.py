"""
3536. Maximum Products of Two Digits
Level: Easy
Topics: Math, Sorting
Link: https://leetcode.com/problems/maximum-product-of-two-digits?envType=problem-list-v2&envId=math
Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def maxProduct(self, n: int) -> int:
        res = 1
        largest = secondLargest = 0
        while n:
            rem = n % 10 
            if rem > largest:
                secondLargest = largest
                largest = rem 
            elif rem > secondLargest:
                secondLargest = rem
            n = n // 10 
        res = largest * secondLargest 
        return res 