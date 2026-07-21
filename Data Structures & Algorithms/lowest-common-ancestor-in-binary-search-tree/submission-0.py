# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    from collections import deque
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        l = self.hasPorQ(root.left, p, q)
        r = self.hasPorQ(root.right, p, q)
        if l and r or ((root.val == q.val or root.val == p.val) and (r or l)):
            return root

        if l:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

    

    def hasPorQ(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        if not root:
            return False

        if root.val == p.val or root.val == q.val:
            return True
        
        return self.hasPorQ(root.left, p, q) or self.hasPorQ(root.right, p, q)


                
        