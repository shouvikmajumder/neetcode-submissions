# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        '''
            Problem Notes: 
                A possible solution is to go throught every node in every list, make a new list in sorted order 
                    Iterate throught the list to creata Newnodes that have the same value 
                        connect all of the new nodes and return the head 
        '''
        node_val_lst = []
        
        for node in lists: 
            curr = node
            
            while curr:
                node_val_lst.append(curr.val)
                curr = curr.next

        
        if node_val_lst:
            node_val_lst.sort()
    
            head = ListNode(node_val_lst[0])
            curr = head

            for val in node_val_lst: 
                node = ListNode(val)
                curr.next = node 
                curr = curr.next 
        
            return head.next
        else: 
            return None
        





