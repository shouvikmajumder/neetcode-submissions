# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # collect the depth on th left and depth on the right and see if the differnce > 2

        def dfs(root):
            stack = [(root,0)]
            height = float('-inf')
            while stack:
                node, level = stack.pop()             
                height = max(height, level)

                if node.right: 
                    stack.append((node.right, level + 1))
                if node.left:
                    stack.append((node.left, level + 1))
            return height
     
        if not root:
            return True
        elif not root.left or not root.right:
            return False

        left_tree,right_tree = dfs(root.left), dfs(root.right)
        return abs(left_tree - right_tree) < 2        
