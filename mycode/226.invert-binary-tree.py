#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# Definition for a binary tree node.
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def visit(node):
            if not node:
                return

            if node.left or node.right:
                node.left, node.right = node.right, node.left

                if node.left:
                    visit(node.left)
                
                if node.right:
                    visit(node.right)
            
            return node
        
        return visit(root)
        
# @lc code=end
