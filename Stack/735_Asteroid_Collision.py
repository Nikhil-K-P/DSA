"""
735. Asteroid Collision
Level: Medium
Topics: Stack, Array, Simulation
Link: https://leetcode.com/problems/asteroid-collision?envType=problem-list-v2&envId=stack
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroid):
                    break
            else:
                stack.append(asteroid)
        return stack