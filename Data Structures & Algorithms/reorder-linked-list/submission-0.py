# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head 
        if curr == None: 
            return 
        nodes = []

        while curr: 
            nodes.append(curr)
            curr = curr.next

        # going to do 2 pointers

        left, right = 0, len(nodes) - 1

        while(left < right):

            nodes[left].next = nodes[right]

            left += 1

            nodes[right].next = nodes[left]

            if left >= right:
                break

            right -= 1

        nodes[left].next = None

            


