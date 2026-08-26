# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        InorderOutput = []

        def dfs(root): 
            if not root:
                return 

            dfs(root.left)
            InorderOutput.append(root.val)
            dfs(root.right)

        dfs(root)

        return InorderOutput

    



        