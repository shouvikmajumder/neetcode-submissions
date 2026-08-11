# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root):

            stack = [root]
            
            visited = []

            while stack: 
                node = stack.pop()
                visited.append(node)

                if node.right: 
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return visited

        stack = [root]
        ancestor_lst = []
        while stack:
            node = stack.pop()
            if node.val == p.val or node.val == q.val: 
                return node
            if node.val < p.val and node.val < q.val: #right side of the tree
                stack.append(node.right)
            if node.val > p.val and node.val > q.val:
                stack.append(node.left) 
            # means that p and q are in different trees
            if node.val > q.val and node.val < p.val or node.val < q.val and node.val > p.val: 
                left_side, right_side = dfs(node.left), dfs(node.right)
                
                index = min(len(left_side), len(right_side))

                for i in range(index):
                    node1, node2 = left_side[i] , right_side[i]
                    
                    if node1.val == node2.val:
                        ancestor_lst.append(node1)
                if ancestor_lst == []:
                    return node 
                return ancestor_lst[-1]
                

                


