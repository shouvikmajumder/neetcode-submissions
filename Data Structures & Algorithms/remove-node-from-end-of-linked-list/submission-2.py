# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        identify_node = []
        curr = head
        while curr:
            identify_node.append(curr)
            curr = curr.next
        
        identify_node_index = len(identify_node) - n

        
        if identify_node[identify_node_index] == head:
            return identify_node[identify_node_index].next 
        else: 
            temp = identify_node[identify_node_index].next 
            prev = identify_node[identify_node_index - 1]
            prev.next = temp 

        return head


        
        

        

        