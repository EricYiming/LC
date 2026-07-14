# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True

        def findHeight(root): 
            if root is None: 
                return 0
            else: 
                left_height = findHeight(root.left)
                right_height = findHeight(root.right)
                if abs(left_height - right_height) > 1: 
                    nonlocal flag
                    flag = False
                    return 0
                return max(left_height, right_height) + 1
        
        findHeight(root)
        return flag
        