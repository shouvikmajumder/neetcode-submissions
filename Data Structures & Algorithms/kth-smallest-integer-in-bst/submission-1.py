from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        queue = deque([root])

        node_lst = []

        while queue:
            node = queue.popleft()
            node_lst.append(node.val)

            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)

        return sorted(node_lst)[k-1]
            





        
