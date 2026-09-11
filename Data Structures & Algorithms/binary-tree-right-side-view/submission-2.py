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
        res = []
        queue = deque()
        queue.append(root)
        while queue: 
            length = len(queue)
            right = TreeNode()
            for i in range(length): 
                current = queue.popleft()
                if current.left: 
                    queue.append(current.left)
                if current.right: 
                    queue.append(current.right)
                right = current
            res.append(right.val)
        return res
            
            
