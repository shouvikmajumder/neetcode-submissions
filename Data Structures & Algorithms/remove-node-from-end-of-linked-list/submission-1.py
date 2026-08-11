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
        
        if len(identify_node) <= 1:
            return None 
        identify_node = identify_node[::-1][n-1]

        curr2 = head
        
        while curr2:    
            if curr2.next == identify_node: 
                temp = identify_node.next
                curr2.next = temp             
            curr2 = curr2.next
        
        return head
        

        