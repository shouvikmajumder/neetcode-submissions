# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        path = 0
        stack = [root]
        visited = []

        while stack:
            node = stack.pop()
            path += 1
            if node.right:
                stack.append(node.right)
                visited.append([node.right,path])
            if node.left:
                stack.append((node.left))
                visited.append([node.left,path])


        return (visited.pop()[1])
                      