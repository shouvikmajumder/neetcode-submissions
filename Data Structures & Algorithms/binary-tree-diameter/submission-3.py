# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        '''
            Problem Notes: 

                Do a recursive dfs down the tree

                return up the max of 1 + max(leftNode,righNode) untill not root 

        '''

        nodes = {"left": [], "right": []}

        stack = [[root,1]]

        while stack: 
            node, level = stack.pop()

            if node.right:
                nodes["right"].append(level)
                stack.append([node.right, level + 1])
            if node.left: 
                nodes["left"].append(level)
                stack.append([node.left, level + 1])

        
        return min(nodes["left"]) + min(nodes["right"])
 
