# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        q = deque()
        q.append(root)
        res = []

        while q: 
            length = len(q)
            item = None
            for _ in range(length): 
                parent = q.popleft()
                item = parent.val
                if parent.left: 
                    q.append(parent.left)
                if parent.right: 
                    q.append(parent.right)
            res.append(item)
        return res


        