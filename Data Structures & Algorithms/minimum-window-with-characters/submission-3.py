class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # manage edge cases
        if len(s) < len(t): 
            return ""
        elif t == "": 
            return ""
        else:
            #initialize a hashmap for T as well as one for strings 
            window, freqCountT = {},{}     

            for char in t:  
                if char not in freqCountT:
                    freqCountT[char] = 1
                elif char in freqCountT:
                    freqCountT[char] +=1 
            #sliding window
            need = len(freqCountT)
            have = 0
            left = 0
            res, res_len = [-1 ,-1], float("inf")            
            for right in range(len(s)):
                char = s[right]
                
                if char not in window: 
                    window[char] = 1
                elif char in window: 
                    window[char] += 1
                
                if char in freqCountT and freqCountT[char] == window[char]:
                    have +=1 

                while need == have:
                    #basically you have a sol but dont know yet if it is the minWindow 
                    #this is just checking what out subwindow is going to be
                    if right - left + 1  < res_len: 
                        res_len = right - left + 1
                        res = [left,right]          

                    # now we have to decerement the left pointer to see if we have a better sol   
                    window[s[left]] -= 1
                    if s[left] in freqCountT: 
                        have -= 1
                        #this would then effectively break the loop if the window isnt there
                    left += 1
            # we needed res_len to make sure that the window that we have was the smallest
            # res have us the indexs to return the substr

        left_index,right_index = res

        return s[left_index: right_index + 1]
            
                    
                    





            