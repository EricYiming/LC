# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0
        def findHeight(root): 
            nonlocal diameter
            if root is None: 
                return 0
            else: 
                left_max = findHeight(root.left)
                right_max = findHeight(root.right)
                diameter = max(left_max + right_max, diameter)
                return max(left_max, right_max) + 1
        
        
        left_max = findHeight(root.left)
        right_max = findHeight(root.right)
        diameter = max(left_max + right_max, diameter)
        return diameter
        