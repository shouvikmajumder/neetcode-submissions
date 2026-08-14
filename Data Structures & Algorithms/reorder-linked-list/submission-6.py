# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
            Problem Approach/Notes: 
                We are going to iterate throught the input linkedlst and store the notes 
                in a list datastructure

                We can create an output array which is going to have reordered nodes

                Core logic:
                    we are going to have 2 pointer that is going to alternate adding nodes to the   
                    output array from the front of the list and the end of the lst 

                    Once we have all of our nodes, we can go ahead an update the pointer to the nodes 
                    accordingly

                Key Note: You dont have to return anything and make sure to append None
                 or else you will get a cycle
        """ 

        # add nodes to a list, where we can then use a two pointer apporach to relink the list 
        # to the corresponding nodes

        nodes_lst = []
        curr = head

        while curr:
            nodes_lst.append(curr)
            curr = curr.next

        left, right = 0 , len(nodes_lst) - 1 

        ordered_lst = []
        while left <= right:
            ordered_lst.append(nodes_lst[left])
            ordered_lst.append(nodes_lst[right]) 
            left += 1
            right -= 1

        if len(ordered_lst) == 1: 
            return ordered_lst[0]
            
        curr = ordered_lst[0]
        print(curr.val)
        for index in range(1, len(ordered_lst)): 
            node = ordered_lst[index]
            curr.next = node
            curr = curr.next
        
        curr.next = None


            

        


        

