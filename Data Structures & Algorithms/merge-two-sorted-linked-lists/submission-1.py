# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_node_head = ListNode()
        new_node_tail = new_node_head

        while list1 and list2:

            if list1.val <= list2.val: 
                new_node_tail.next = list1
                list1 = list1.next
            else:
                new_node_tail.next = list2
                list2 = list2.next

            new_node_tail= new_node_tail.next
        
        if list1:
            new_node_tail.next = list1
        else: 
            new_node_tail.next = list2 
        
        return new_node_head.next
    
        

        
                