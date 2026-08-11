# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #collect all of the noes in an array and perform two pointers

        curr = head
        
        nodes_lst = []

        while curr: 
            nodes_lst.append(curr)
            curr = curr.next
        
        left, right = 0, len(nodes_lst) - 1

        while(left < right):
            #want to set the left node to the right node 
            nodes_lst[left].next = nodes_lst[right]
            left += 1

            #also need to check if the left and right arnt pointing to the same node
            if left == right:
                break

            nodes_lst[right].next =nodes_lst[left]
            right -= 1
            
        nodes_lst[left].next = None
    


