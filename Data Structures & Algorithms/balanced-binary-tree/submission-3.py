# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0

            lb, lh = dfs(root.left)
            rb, rh = dfs(root.right)

            balanced = abs(rh - lh) <= 1 and lb and rb
            return balanced, 1 + max(rh, lh)

        return dfs(root)[0]
        
