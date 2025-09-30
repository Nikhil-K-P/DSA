"""
412. Fizz Buzz
Level: Easy
Topics: Array, String, Simulation
Link: https://leetcode.com/problems/fizz-buzz?envType=problem-list-v2&envId=string
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 5 == 0:
                res.append('Buzz')
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i))
        return res
