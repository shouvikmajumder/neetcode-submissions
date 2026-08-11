# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_side = self.get_height(root.left)
        right_side = self.get_height(root.right) 
        
        if abs(left_side - right_side) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right) 
            

    def get_height(self, root): 

        if not root: 
            return 0    

        return 1 + max(self.get_height(root.left),self.get_height(root.right))

