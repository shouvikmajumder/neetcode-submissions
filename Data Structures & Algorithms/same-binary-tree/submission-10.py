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
            node1_right = node1.right if node1.right else None 
            node2_right = node2.right if node2.right else None 
            stack.append((node1_right,node2_right))
            
            node1_left = node1.left if node1.left else None
            node2_left = node2.left if node2.left else None
            stack.append((node1_left,node2_left))

            
        