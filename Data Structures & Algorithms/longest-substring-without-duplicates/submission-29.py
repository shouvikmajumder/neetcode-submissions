class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            Problem Approach: 
                I would use a set where, while using a two pointer approach 
                Algorithm in a nutshell: 
                    - We are basically going to increment the right pointer and add any unseen elements
                    to a visited set and increment the counter
                    - Once we see an element that we have seen before we increment left
                    pointer as well as decrement the counter                 
                    - Every pass we also want to check that we are updating the global max counter
        '''

        if len(s) == 0: 
            return 0
        else: 
            left = 0
            char_counter = 0
            max_char_counter = 0
            visited = set()

            for i in range(len(s)): 
                right = s[i]
                
                #if you encounter a duplicate
                while right in visited:
                    visited.remove(s[left])
                    left +=1 
                    char_counter -=1
                if right not in visited: 
                    visited.add(right)
                    char_counter += 1
                
                max_char_counter = max(max_char_counter,char_counter)
            
            return max_char_counter