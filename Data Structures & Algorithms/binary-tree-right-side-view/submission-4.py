# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        level_visited_left = {1:[root.val]}
        level_visited_right = {1:[root.val]}

        #dfs approach

        stack = [(root,1)]

        while stack:
            node, level = stack.pop()

            if not node: 
                continue
            
            if node.right:
                stack.append((node.right, level + 1))
                if level + 1 not in level_visited_right: 
                    level_visited_right[level + 1] = []
                level_visited_right[level + 1].append(node.right.val)

                
            if node.left: 
                stack.append((node.left, level + 1))

                if level + 1 not in level_visited_left:
                    level_visited_left[level + 1] = []
                level_visited_left[level+1].append(node.left.val)
        
        print(level_visited_left)
        print(level_visited_right)

        max_index = max(len(level_visited_left),(len(level_visited_right))) 

        print(max_index)

        level = 1

        output_lst = []

        while(level <= max_index): 
            
            if level in level_visited_right:
                val = (level_visited_right[level][-1])
                output_lst.append(val)
            else:
                val = (level_visited_left[level][-1])
                output_lst.append(val)

            level += 1

        return output_lst





