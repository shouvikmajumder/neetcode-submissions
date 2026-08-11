# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        # run a dfs
        # terminating conditions are if node.left > root or node.right < root

        stack = [root]

        while stack:
            
            node = stack.pop()
            
            if node.right: 

                if node.right.val < node.val: 
                    return False
                stack.append(node.right)
                
            if node.left: 
                if node.left.val >= node.val: 
                    return False
                stack.append(node.left)
        

        return True
