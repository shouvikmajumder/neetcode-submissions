# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        stack = [root]

        while stack: 
            node = stack.pop()

            if node.val == p.val or node.val == q.val or node.left.val == p.val and node.right.val == q.val:
                return node
            
            if p.val > node.val and q.val > node.val: #both greater go right
                stack.append(node.right)
            if p.val < node.val and q.val < node.val: #both less go left
                stack.append(node.left)
        
        