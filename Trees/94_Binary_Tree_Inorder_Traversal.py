"""
94. Binary Tree Inorder Traversal
Level: Easy
Topics: Tree, Stack, Binary Tree, Depth-First Search
Link: https://leetcode.com/problems/binary-tree-inorder-traversal?envType=problem-list-v2&envId=stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
        dfs(root)
        return stack