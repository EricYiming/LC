# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 

        def dfs(node): 
            nonlocal count

            if node.left: 
                output = dfs(node.left)
                if output: 
                    return output
            
            count += 1
            if count == k: 
                return node.val
            
            if node.right: 
                output = dfs(node.right)
                if output: 
                    return output

        return dfs(root)
        