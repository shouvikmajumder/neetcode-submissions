# Definition for singly-linked list.
# class ListNode:
#     def __init__(_NoDefaultType, self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        nodelstl1,nodelstl2 = "",""
        curr = l1
        while curr: 
            nodelstl1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr: 
            nodelstl2 += str(curr.val)
            curr = curr.next
        total = int(nodelstl1[::-1]) + int(nodelstl2[::-1])
        print(total)

        new_node_lst = []
        
        for i in str(total)[::-1]: 
            new_node_lst.append(ListNode(int(i)))

        curr = new_node_lst[0]    
        print(curr.val)

        for index in range(1,len(new_node_lst)):
            node = new_node_lst[index]
            curr.next = node
            curr = curr.next 
        
        curr.next = None

        return new_node_lst[0]


        
