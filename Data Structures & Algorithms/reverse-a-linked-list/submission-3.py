# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head #copying LL so that links are preserved

        while curr != None: 
            temp = curr.next #basically saving the value to relink later
            
            curr.next = prev 
            prev = curr
        
            curr = temp
        
        return prev
            



            





