# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_linked_list = ListNode()
        curr = new_linked_list
        carry = 0 

        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            #adding the values and putting it into a node
            value = val1 + val2 + carry
            carry = value // 10
            value = value % 10
            print(value)
            #create and add the node into the Linked List 
            node = ListNode(value)
            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None


        return new_linked_list.next
