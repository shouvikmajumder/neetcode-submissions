# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: 
            return True
        elif q and not p or p and not q: 
            return False
        else: 
            stack_p, stack_q = [p],[q] 

            while stack_p and stack_q: 
                node_p,node_q = stack_p.pop(), stack_q.pop()

                if node_p and node_q: 
                    if node_p.val != node_q.val:
                        return False
                elif not node_p and node_q or not node_q and node_p:
                    return False

                if node_p.right:
                    stack_p.append(node_p.right)
                if node_p.left: 
                    stack_p.append(node_p.right)
                if node_q.right:
                    stack_q.append(node_q.right)
                if node_q.left:
                    stack_q.append(node_q.left) 


            return True
