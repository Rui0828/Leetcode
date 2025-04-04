#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, depth):
        if node.left and node.right:
            r_node, r_depth = self.dfs(node.right, depth + 1)
            l_node, l_depth = self.dfs(node.left, depth + 1)

            if r_depth == l_depth:
                return node, r_depth
            elif r_depth > l_depth:
                return r_node, r_depth
            else:
                return l_node, l_depth
        elif node.left:
            return self.dfs(node.left, depth + 1)
        elif node.right:
            return self.dfs(node.right, depth + 1)
        else:
            return node, depth

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans, _ = self.dfs(root, 0)
        return ans
# @lc code=end

