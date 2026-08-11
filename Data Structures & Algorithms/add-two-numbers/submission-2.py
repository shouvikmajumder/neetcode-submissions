# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases largly with the carries    

        output_linked_lst = ListNode()
        curr = output_linked_lst
        carry = 0
        while l1 or l2 or carry: 

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # need to handle the carries
            val  = v1 + v2 + carry
            carry = val // 10 
            val = val % 10 

            newnode = ListNode(val)
            curr.next = newnode
            curr = curr.next

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 


        return output_linked_lst.next
            










