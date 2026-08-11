# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        concat_l1 = ""
        concat_l2 = ""


        while l1 and l2: 
            concat_l1 += str(l1.val)
            concat_l2 += str(l2.val) 

            l1 = l1.next
            l2 = l2.next 
        
        res = int(concat_l1[::-1]) + int(concat_l2[::-1])
        ordered_res = str(res)[::-1]
        
        output_arr = []

        for i in ordered_res: 
            newnode = ListNode(int(i))
            output_arr.append(newnode)

        if len(output_arr) == 1: 
            return output_arr[0].val

        for i in range(1,len(output_arr)): 
            output_arr[i-1].next = output_arr[i]
        
        return output_arr[0]








