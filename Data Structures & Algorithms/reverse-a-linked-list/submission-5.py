# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head 
        prev = None  

        while curr != None: 
        
            temp = curr.next #save link to the next node
            curr.next = prev
            prev = curr
            curr = temp #progressing the linked list

        return prev
