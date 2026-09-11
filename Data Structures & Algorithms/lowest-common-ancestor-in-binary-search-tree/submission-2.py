# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == root.val: 
            return p
        if q.val == root.val: 
            return q
        low = p.val if p.val < q.val else q.val
        high = p.val if p.val > q.val else q.val
        if low < root.val < high: 
            return root
        elif low < root.val and high < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif low > root.val and high > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        
        