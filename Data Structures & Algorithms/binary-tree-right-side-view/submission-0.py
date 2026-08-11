# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        stack = [root]

        visited = set()

        while stack:
            
            node = stack.pop()
            visited.add(node.val)

            if node.right:
                stack.append(node.right)

        return list(visited)