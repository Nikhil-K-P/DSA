"""
2180. Count Integers With Even Digit Sum
Level: Easy
Topics: Math, Simulation
Link: https://leetcode.com/problems/count-integers-with-even-digit-sum?envType=problem-list-v2&envId=math
Time Complexion: O(n log n)
Space Complexion: O(1)
"""


class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            digitSum = 0
            num = i
            while num:
                digitSum += num % 10 
                num = num // 10 
            if digitSum % 2 == 0:
                count += 1
        return count 