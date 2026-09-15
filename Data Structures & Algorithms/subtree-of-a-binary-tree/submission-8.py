from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # dfs on root untill we get subroot
        # call a helper that determines if it is a subtree 
        # if not return     

        def bfs(root):
            queue = deque([root])
            output = []
            while queue:
                node = queue.popleft()
                output.append(node.val)

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            return output

        if not root and not subRoot:
            return True 
        if not root or not subRoot:
            return False
        
        stack = [root]

        while stack: 
            node = stack.pop()

            if node.val == subRoot.val:
                if (bfs(node) == bfs(subRoot)):
                    return True
                else:
                    continue

            if node.right:
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
            
        return False












