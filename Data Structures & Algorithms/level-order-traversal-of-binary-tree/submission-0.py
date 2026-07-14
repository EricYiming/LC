# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        q = deque()
        q.append(root)
        res = []

        while q: 
            level = []
            n = len(q)
            for _ in range(n): 
                parent = q.popleft()
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
                level.append(parent.val)
            res.append(level)
        return res
            

        