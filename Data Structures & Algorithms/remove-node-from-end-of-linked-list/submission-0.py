# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n - 1 

        curr = head

        nodes = []

        while curr: 
            nodes.append(curr)
            curr = curr.next

        target_index = len(nodes) -n

        target_node = nodes[target_index]

        if target_index == 0: 
            return head.next
            
        prev_nodes = nodes[target_index - 1]

        temp = target_node.next
        
        prev_nodes.next = temp

        return head
        
