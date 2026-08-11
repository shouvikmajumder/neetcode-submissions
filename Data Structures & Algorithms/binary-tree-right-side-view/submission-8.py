from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
             You can perform a bfs and store all of the nodes on that level in an array and append the right most element
             to an output list

             since the output type its expecting is a list of ints we can appened the value of the nodes
             and return it as the output
        '''

        if not root:
            return []

        res =[]

        stack = [[root,0]]
    
        while stack: 
            
            node,depth = stack.pop()

            if depth == len(res): 
                res.append(node.val)

            if node.left: 
                stack.append([node.left, depth + 1])
            if node.right:      
                stack.append([node.right, depth + 1])

        return res 

            




