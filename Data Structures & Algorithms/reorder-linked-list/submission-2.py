# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        reorder_lst = []
        curr = head
        
        while curr: 
            reorder_lst.append(curr)
            curr = curr.next
        
        left,right = 0, len(reorder_lst) -1
        
        while left < right:
            reorder_lst[left].next = reorder_lst[right]
            left += 1

            if left >= right: 
                break
            
            reorder_lst[right].next = reorder_lst[left]
            right -= 1 

        reorder_lst[left].next = None 
        

    
    