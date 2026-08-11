# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        pre: [1,2,3,4] 
        in: [2,1,3,4] left [1: root] right: [root+1 : ]

        pre: [4, 2, 1, 3, 6, 5, 7]
        in : [1, 2, 3, 4, 5, 6, 7]

        '''
        if not preorder and not inorder: 
            return

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) #gives the index of the root node

        root.left = self.buildTree(preorder[1:mid +1],inorder[ : mid])
        root.right = self.buildTree(preorder[mid + 1: ],inorder[mid + 1:])


        return root