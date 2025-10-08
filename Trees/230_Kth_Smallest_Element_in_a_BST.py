"""
230. Kth Smallest Element in a BST
Level: Medium
Topic: Tree, Depth-First Search, Binary Search Tree
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst
Time Complexity: O(h + k) where h is the height of the tree
Space Complexity: O(h) where h is the height of the tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        K = 0 
        res = 0
        def dfs(root):
            nonlocal K, res
            if not root:
                return 
            dfs(root.left)
            K += 1
            if K == k:
                res = root.val
            dfs(root.right)
        dfs(root)
        return res