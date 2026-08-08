# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        if root:
            q = deque([root])
            while q:
                curr_node = None
                for _ in range(len(q)):
                    curr_node = q.popleft()
                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
                res.append(curr_node.val)

        return res
