"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
            Problem Approach:
                The core logic is going to be very similar to deep clone linked list problem, however
                instead of a random pointer we have neighbors instead 

                We are going to init a hashmap where the key is going to be the original node 
                and the value is going to be the copy of the original node

                we are going to run a dfs where if we have seen a copy already we want to return 
                out of the recursive call 

                in order to form a deep copy of the nodes, we can iterate through the negihbors of 
                the original node negihbors and make a dfs call on each of the neighbors 

                we can return copy as a result if there is a node that exists
        '''

        orig_to_copy = {}

        def clone(node): 
            if node in orig_to_copy: 
                return orig_to_copy[node]
            copy = Node(node.val)
            orig_to_copy[node] = copy
            #we have a copy of the node but we still have to copy the neihbors
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy
            
            
        if node: 
            return clone(node)
        return node

        

            






