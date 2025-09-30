"""
100. Same Tree
Level: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: https://leetcode.com/problems/same-tree
Time Complexity: O(min(m, n))
Space Complexity: O(min(m, n))
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False