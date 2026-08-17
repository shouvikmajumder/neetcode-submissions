# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Problem Approach/ Notes:
                We would need to first create a new linkedlist and append the new added nodes together
                also we need to consider adding the carry bit if the number overflows for exmaple 

                if we add 4 and 8 we get 12 
                but 12 would need to get split into 2 nodes: 2 --> 1

                key trick here is to add all of the values of l1 l2 and the prev carry bit if there is one 

                value // 10 gives you the last number, which is going to be the carry (if you remember its reversed 2 --> 1)
                value % 10 gives you the front digit which you are going to connect to the newlist 

        '''
        outputlst = ListNode() 
        carry = 0 
        curr = outputlst

        while l1 or l2 or carry: 
            val_1 = l1.val if l1 else 0            
            val_2 = l2.val if l2 else 0

            value = val_1 + val_2 + carry
            carry = value // 10
            value = value % 10

            newnode = ListNode(value)
            curr.next = newnode
            curr = curr.next

            # need to progress l1 ad l2

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        return outputlst.next




