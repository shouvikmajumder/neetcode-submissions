"""
# Definition for a Node.
class Node:, NoDefault
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':  
        '''
            Problem Approach/Notes: 
                Since nodes are unique we can use the node as a key and a newnode as the value 
                we can create a newlist havcing the dict.values()[0] as the head and link all of the nodes  
                accordingly

                Still have to consider the Null condition, so we probably have to initialzie the dict as {None:None}
                    

            Key Problem faced: The input contains the index not the actual node it wants to point to
        '''
        node_mappings = {None:None}
        curr = head

        while curr: 
            node_copy = Node(curr.val)
            node_mappings[curr] = node_copy
            curr = curr.next

        # no we need to build the lst

        curr = head
        
        while curr: 
            node_copy = node_mappings[curr]
            node_copy.next = node_mappings[curr.next]
            node_copy.random = node_mappings[curr.random]
            
            curr = curr.next
            
        return node_mappings[head]
            

