"""
110. Balanced Binary Tree
Level: Easy
Topics: Tree, Depth-First Search, Binary Tree, Recursion
Link: https://leetcode.com/problems/balanced-binary-tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [isBalanced, 1 + max(left[1], right[1])]
        res = dfs(root)
        return res[0]