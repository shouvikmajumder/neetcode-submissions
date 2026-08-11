class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited = set()

        left = 0 

        counter = 0
        max_counter = 0

        for i in range(len(s)): 
            right= s[i]
            
            while right in visited: 
                counter -= 1 
                visited.remove(s[left])
                left += 1
            
            if right not in visited: 
                counter += 1
                visited.add(right)

            max_counter = max(max_counter, counter)                

        return max_counter