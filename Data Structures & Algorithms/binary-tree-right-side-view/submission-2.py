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

            #only for debug
            if node != None:
                print(node.val)

            if node == None:
                continue

            visited.add(node.val)
            if node.right:
                stack.append(node.right)

            if not node.right: 
                stack.append(node.left)

        return list(visited)