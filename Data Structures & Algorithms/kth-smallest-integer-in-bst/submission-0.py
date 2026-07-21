# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort = []
        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)
            if len(sort) == k:
                return
            sort.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(sort)
        return sort[-1]