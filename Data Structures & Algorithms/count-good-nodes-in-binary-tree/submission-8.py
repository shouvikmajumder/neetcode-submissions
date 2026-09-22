# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # need some way to track teh max weve seen so far 
        if not root: 
            return 0

        good_node_counter = 0
        stack = [(root,root.val)]

        while stack:
            node, current_max = stack.pop()

            if node.val >= current_max:
                good_node_counter += 1 
            current_max = max(node.val,current_max)


            if node.right:
                stack.append((node.right,current_max))
            if node.left:
                stack.append((node.left,current_max))

        return good_node_counter