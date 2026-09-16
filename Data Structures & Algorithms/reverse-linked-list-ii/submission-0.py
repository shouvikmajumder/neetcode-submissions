# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        node_lst = []
        
        curr = head

        left_index = left - 1
        right_index = right - 1
        while curr:
            node_lst.append(curr)
            curr = curr.next   
        
        node_lst[left_index: right_index + 1] = node_lst[left_index: right_index + 1][::-1]
        
        head = node_lst[0]
        curr = head
        for node in node_lst[1:]:
            curr.next = node
            curr = curr.next 
        curr.next = None 

        return head