# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, total):
            if not node:
                return False

            new_total = total + node.val
            if node.left or node.right:
                left = dfs(node.left, new_total)
                right = dfs(node.right, new_total)
                return left or right
            
            return new_total == targetSum
        
        return dfs(root, 0)
                