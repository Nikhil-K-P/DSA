"""
1337. The K Weakest Rows in a Matrix
Level: Easy 
Topics: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix 
Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix?envType=problem-list-v2&envId=heap-priority-queue
Time Complexity: O(m * n)
Space Complexity: O(m + n)
"""
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        rows, cols = len(mat), len(mat[0])
        soldiers = [[] for i in range(cols + 1)]
        res = []
        for r in range(rows):
            count = 0
            for c in range(cols):
                if mat[r][c] == 1:
                    count += 1
            soldiers[count].append(r)

        n = len(soldiers)
        for i in range(n):
            for row in soldiers[i]:
                res.append(row)
                if len(res) == k:
                    return res
        return res
    