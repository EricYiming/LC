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
        res = []
        queue = deque()
        queue.append(root)
        while queue: 
            length = len(queue)
            level = []
            for i in range(length): 
                target = queue.popleft()
                level.append(target.val)
                if target.left: 
                    queue.append(target.left)
                if target.right: 
                    queue.append(target.right)
            res.append(level)
        return res

        