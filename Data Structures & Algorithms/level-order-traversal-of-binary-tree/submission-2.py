from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # every level is unique, so we can use it to make a key value pair
        #key is going to be the level , val is a list that contains the nodes in the level

        if not root:
            return []

        queue = deque([[root,1]])

        node_collections = {}
        
        while queue: 
            
            node, level = queue.popleft()

            print(node,level)
            
            if level not in node_collections: 
                node_collections[level] = [node.val]
            elif level in node_collections: 
                node_collections[level].append(node.val)

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])



        return list(node_collections.values())
        

