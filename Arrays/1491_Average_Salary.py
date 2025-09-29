"""
1491. Average Salary Excluding the Minimum and Maximum Salary
Level: Easy
Topics: Array, Math
Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary?envType=problem-list-v2&envId=sorting
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def average(self, salary: list[int]) -> float:
        n = len(salary)
        salarySum = 0
        minSal = float('inf')
        maxSal = float('-inf')
        for s in salary:
            if s < minSal:
                minSal = s
            if s > maxSal:
                maxSal = s
            salarySum += s

        averageS = (salarySum - (minSal + maxSal)) / (n - 2)
        return averageS