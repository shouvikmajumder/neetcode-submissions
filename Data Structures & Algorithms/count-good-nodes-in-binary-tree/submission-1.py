# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            path from the root to a node(x) there cant be any node value thats greater than node(x)

            there could be multiple so you have to have a counter whenever you find a correct case

            we are going to use a dfs to traverse the tree and do not necessarily need to keep track
            
            of the path we just need to run into a root thats greater than the current max
                         
        '''

        curr_max = 0

        stack = [[root,root.val]]

        good_node_count = 0
    
        while stack:    

            node,val = stack.pop()

            if val >= curr_max: 
                good_node_count += 1

            curr_max = max(curr_max,val) 
    
            if node.right: 
                stack.append([node.left, node.right.val])
            
            if node.left:
                stack.append([node.left, node.left.val])
                

        return good_node_count