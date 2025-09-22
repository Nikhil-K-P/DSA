"""
71. Search a 2D Matrix
Level: Medium
Topics: Array, Binary Search
Link: https://leetcode.com/problems/search-a-2d-matrix
Time Complexity: O(log(m) + log(n)) = O(log(mn))
Space Complexity: O(1)
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        while left <= right:
            row = left + (right - left) // 2
            if target > matrix[row][-1]:
                left = row + 1
            elif target < matrix[row][0]:
                right = row - 1
            else:
                break 
        if not left <= right:
            return False

        left, right = 0, n - 1
        while left <= right:
            col = left + (right - left) // 2
            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] < target:
                left = col + 1
            else:
                right = col - 1
        return False