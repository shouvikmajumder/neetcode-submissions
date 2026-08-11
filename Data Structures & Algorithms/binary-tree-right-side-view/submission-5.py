# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue =[root]
        res = []


        while queue:

            right_node = None
            level = len(queue)

            for i in range(level):
                node = queue.pop(0)

                if node: 
                    #going to get updated as you go through thte nodes at a particular level
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_node: 
                res.append(right_node.val)
        
        return res
        
                