# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = [root]

        res = []

        while queue: 
            
            level = len(queue) 
            right_most = None

            for node in range(level):
                node = queue.pop(0)
                if node: 
                    right_most = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if right_most:   
                res.append(right_most.val)
        return res







