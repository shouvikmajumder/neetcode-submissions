# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # split the tree by checkign if rootleft and root.right exist
        # run a dfs on both trees which should return the height
        # compare the heights if their difference is >1 then you return False else return True 

        def dfs(root): 
            if not root: 
                return 0
            stack = [[root, 0]]
            tree_height = 0

            while stack: 
                node, height = stack.pop()

                tree_height = height

                print(tree_height)   

                if node.right: 
                    stack.append([node.right, height + 1])
                if node.left: 
                    stack.append([node.left, height + 1])
                

            return tree_height

        if not root:
            return True
        else:      

            height_left_subtree, height_right_subtree = dfs(root.left) , dfs(root.right)

            # if the differnece is > 1 then you return False 

            difference = abs(height_left_subtree - height_right_subtree)
            print(difference)

            if difference > 1: 
                return False
            return True
        