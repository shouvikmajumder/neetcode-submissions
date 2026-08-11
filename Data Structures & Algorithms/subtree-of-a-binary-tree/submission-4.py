# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Notes on how to solve:

        1) Dfs traversal throught the root untill you have a same value node as the subRoot
        
        2) develop a helper funciton that basically runs another dfs to see if the trees
           are the same from that point, return True otherwise dont return anything

        3) return False at the end if every traversal went through

        '''
        def isSameTree(root1,root2):
            stack = [[root1,root2]]

            while stack: 
                node1,node2 = stack.pop()
                
                if not node1 and not node2:
                    continue
                elif not node1 or not node2 or node1.val != node2.val: 
                    return False

                if node1.right or node2.right:
                    stack.append([node1.right,node2.right])
                if node1.left or node2.right: 
                    stack.append([node1.left,node2.left])

            return True
            
        stack = [root]

        while stack: 
            node = stack.pop()
            if node.val == subRoot.val: 
                if isSameTree(node,subRoot):
                    return True
                elif not isSameTree:
                    continue

            if node.right:
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)

        return False
















