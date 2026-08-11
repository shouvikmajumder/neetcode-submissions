# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            stack = [root]
            visited = []

            while stack:
                node = stack.pop()
                visited.append(node)
            
                if node.right:
                    stack.append(node.right)
             
            print(visited)
            return visited

        p_output, q_output = dfs(p), dfs(q)

        for i in range(len(p_output)):
            p_node, q_node = p_output[i], q_output[i]
            
            if not p_node and not q_node:
                continue
            if p_node or q_node or p_node.val != q_node.val: 
                return False
    
        return True