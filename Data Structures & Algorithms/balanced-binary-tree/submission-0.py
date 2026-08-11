# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left_lenth = dfs(root.left)
            right_lenght = dfs(root.right) 
            res.append(abs(left_lenth - right_lenght))
            return 1 + max(left_lenth , right_lenght)
        
  
        dfs(root)
        for i in res: 
            if i>1: 
                return False
        return True