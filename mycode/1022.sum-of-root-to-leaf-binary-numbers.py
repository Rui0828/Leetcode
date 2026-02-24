#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def dfs(node, n):
            nonlocal ans
            if not node:
                return

            n = n*2 + node.val
            
            if not node.left and not node.right:
                ans += n
                return

            if node.left:
                dfs(node.left, n)
            
            if node.right:
                dfs(node.right, n)

        dfs(root, 0)

        return ans
# @lc code=end

