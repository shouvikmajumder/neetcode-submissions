# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            #take max of left and max or right add it together for max path 
            if root == None:
                return 0
            
            left = dfs(root.left) # keeps going left untill it cant 
            right = dfs(root.right) # keeps going right untill it cant
 
            diameter = max(diameter, left + right) # 

            height_of_tree = 1 + max(left,right)

            return height_of_tree


        dfs(root)
        return diameter