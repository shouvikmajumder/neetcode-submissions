# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
           From the root node to a node x there cant by any values that are in between that
           are bigger than the good node that we are tryin to find

           A viable solution could be keeping track of the current max that we have
           seen so far and comparing it to the current node value and if there is a 
           node value thats greater than you have found a good node
                    This is because a good node is only determined by the root node and the
                    node you you're on  so if you encounter a bigger node on the journey it 
                    can be counted as well                     
        '''

        if not root:
            return 0

        stack = [(root,0)]
        curr_max = 0
        good_nodes = 0
        while stack:
        
            node , curr_max = stack.pop()

            if node.val >= curr_max: 
                good_nodes += 1 
        
            new_max = max(curr_max,node.val)

            if node.left: 
                stack.append((node.left,new_max))
            if node.right: 
                stack.append((node.right,new_max))

        return good_nodes                

