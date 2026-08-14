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
        '''
            Problem Approach/Notes: 
                I think that we could initialize a hashmap where we keep {originalnode: node_copy}
                We can iterate over the linked list and create copies of the nodes 

                Afterwards we can reiterate over the linkedlist and connect the node copies
        '''
        if not head:
            return None
        node_mappings = {None:None}
        curr = head

        while curr: 
            node_copy = Node(curr.val)
            node_mappings[curr] = node_copy
            curr = curr.next 

        # we can reset the pointer, iterate over the list again and link the copies accordingly
        curr = head
        node_copy_lst = []
        while curr:
            node_copy = node_mappings[curr]
            node_copy.next = node_mappings[curr.next]
            node_copy.random = node_mappings[curr.random]

            node_copy_lst.append(node_copy)
            
            curr = curr.next 
        
        node_copy_lst[-1].next = None
        
        return node_copy_lst[0]


        

