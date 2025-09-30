"""
543. Diameter of Binary Tree
Level: Easy
Topics: Tree, Depth-First Search, Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree
Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def dfs(root):
            nonlocal res
            if not root:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res