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

                Key Note: You dont have to return anything
        """

        nodes_lst = []
        curr = head

        while curr: 
            nodes_lst.append(curr)
            curr = curr.next 
        ouptput_arr = [] #reordered version of the list 
        left,right = 0, len(nodes_lst) - 1

        while left <= right: 
            ouptput_arr.append(nodes_lst[left])
            ouptput_arr.append(nodes_lst[right])
            left +=1 
            right -= 1

        #Now we have to relink the list 
        
        # you have your head pointer which is ouptput_arr[0]

        curr = ouptput_arr[0] 
        ouptput_arr = ouptput_arr[1:]

        for node in ouptput_arr: 
            curr.next = node
            curr = curr.next
        ouptput_arr[-1].next = None         


