"""
226. Invert Binary Tree
Level: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree
Time Complexion: O(n)
Space Complexion: O(h) where h is the height of the tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root