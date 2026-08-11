# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [root]

        root_node_val = root.val

        while stack: 
            node = stack.pop() 

            if node.right: 
                if node.right.val <= node.val or node.right.val <= root_node_val: 
                    return False
                stack.append(node.right)

            if node.left: 
                if node.left.val >= node.val or node.left.val >= root_node_val:
                    return False
                stack.append(node.left)

        return True

            