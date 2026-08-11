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

        nodes_copy = {None:None}

        curr = head
        while curr: 
            newnode = Node(curr.val)
            nodes_copy[curr] = newnode
            curr = curr.next

        curr = head

        while curr: 
            copy = nodes_copy[curr]
            copy.next =  nodes_copy[curr.next]                
            copy.random = nodes_copy[curr.random]
            curr = curr.next
        
        return nodes_copy[head]

    