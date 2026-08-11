from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        # run a dfs
        # terminating conditions are if node.left > root or node.right < root

        if not root:
            return False

        queue = deque([[root, -10000, 10000]])

        while queue: 
        
            node, lower_bound, upper_bound  = queue.popleft()

            if node.val <= lower_bound or node.val > upper_bound:
                return False

            if node.left:
                queue.append([node.left, lower_bound, node.val])
            if node.right: 
                queue.append([node.right,node.val, upper_bound])

        return True
            






