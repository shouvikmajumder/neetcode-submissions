# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def dfs(root_node):
            stack = [root_node]
            visited = []

            while stack:
                node = stack.pop()
                if node not in visited: 
                    visited.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
                
            return visited    

        root_origin, subRoot_origin= dfs(root), dfs(subRoot) #output of 2 lists
        
        print(root_origin, subRoot_origin)

        if len(subRoot_origin) > len(root_origin):
            return False
        
        left, right = 0, len(subRoot_origin) - 1

        while (right<len(root_origin)):
            if root_origin[left:right+1] == subRoot_origin: 
                return True
            left +=1 
            right +=1
        
        return False



