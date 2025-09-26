"""
504. Base 7
Level: Easy
Topics: Math, String
Link: https://leetcode.com/problems/base-7?envType=problem-list-v2&envId=math
Time Complexion: O(log n)
Space Complexion: O(1)
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = []
        n = abs(num)
        while n:
            rem = n % 7 
            res.append(str(rem))
            n = n // 7
        if num < 0:
            res.append('-')
        return ''.join(res[::-1])