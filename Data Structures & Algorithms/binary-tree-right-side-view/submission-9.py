
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_map = {}

        queue = deque([(root, 0)])

        while queue: 
            node,level = queue.popleft()

            if level not in level_map:
                level_map[level] = [node]
            else: 
                level_map[level].append(node)

            if node.left:
                queue.append((node.left,level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        right_side_nodes = []

        for level in level_map:
            right_side_nodes.append(level_map[level][-1].val)
        
        return right_side_nodes
