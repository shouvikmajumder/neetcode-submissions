# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        stack = [(root,1)]

        visited = {}

        while stack: 
            node , level = stack.pop(0)

            if not node: 
                continue
            if level not in visited: 
                visited[level] = [node.val]
            elif level in visited: 
                visited[level].append(node.val)


            if node.left:
                stack.append((node.left, level + 1))
            
            if node.right:
                stack.append((node.right, level + 1))

        
        return (list(visited.values()))
