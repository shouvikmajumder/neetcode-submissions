from collections import deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            Problem approach/Notes: 
                Quick edge case check: 
                    if len(s1) > len(s2) you would return false because its impossible to have a    
                    substring of another substring that is smaller
                Otherwise: 
                    you can creat a set for s1 and we can perform a sliding window approach where we have a left and right 
                    pointer that start at 0,0. 
                    We increment the right pointer untill we reach a point where the lenght is == to len(s1) while adding the 
                    elements that we have seen so far in a set as well

                    we are going to compare both of the sets and if they are == you would return True



        '''

        if len(s1) > len(s2): 
            return False
        
        s1_lst = list(s1)
        s1_lst.sort()
        comparator = deque([])
        left = 0

        for right in range(len(s2)):
            comparator.append(s2[right])

            #we need a way to check if the comparator is == to s1_lst 
            if sorted(list(comparator)) == s1_lst: 
                return True 
            
            while len(comparator) >= len(s1_lst): 
                comparator.popleft() 
                left +=1 
        return False

















        






