# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root:
            return True

        if not subRoot or not root:
            return False

        def bfs_match(root, subRoot):
            q2 = deque([(root, subRoot)])
            while q2:
                r_c, s_c = q2.popleft()
                if (r_c and s_c and r_c.val != s_c.val
                or (r_c and not s_c or not r_c and s_c)):
                    return False
                if r_c and s_c:
                    if r_c.left or s_c.left:
                        q2.append((r_c.left, s_c.left))
                    if r_c.right or s_c.left:
                        q2.append((r_c.right, s_c.right))
            return True

        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                if bfs_match(curr, subRoot):
                    return True
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return False


