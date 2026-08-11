"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        node_mappings = {None:None}
        curr = head

        while curr: 
            newnode = Node(curr.val)
            node_mappings[curr] = newnode
            curr = curr.next
        curr = head

        while curr: 
            node_copy = node_mappings[curr]
            node_copy.next = node_mappings[curr.next]
            print(curr.random)
            node_copy.random = node_mappings[curr.random] 
            
            curr = curr.next
        
        return node_mappings[head]        



