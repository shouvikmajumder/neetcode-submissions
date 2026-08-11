# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Approach: could prolly do a dfs collect all node and node values and return the node wthe the kth smallest
        # root is garunteed and output type can just be int not TreeNode
        stack = [root]

        output_arr = []

        while stack: 
            node = stack.pop()
            output_arr.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return sorted(output_arr)[k-1]

            
                


