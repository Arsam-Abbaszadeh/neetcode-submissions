# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr, maxVal):
            if not curr:
                return 0
            good_node = 0
            if curr.val >= maxVal:
                good_node = 1
            
            new_max = max(curr.val, maxVal)
            return dfs(curr.left, new_max) + dfs(curr.right, new_max) + good_node
        
        return dfs(root, -101)