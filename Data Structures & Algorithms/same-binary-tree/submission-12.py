# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        
        stack = [(p,q)]

        while stack:
            node1, node2 = stack.pop()

            # print(node1.val,node2.val)
            if not node1 and not node2:
                return True 
            elif not node1 or not node2 or node1.val != node2.val: 
                return False 
            
            if node1.right or node2.right: 
                stack.append((node1.right,node2.right))
            if node1.left or node2.left: 
                stack.append((node1.left,node2.left))

        return True
        