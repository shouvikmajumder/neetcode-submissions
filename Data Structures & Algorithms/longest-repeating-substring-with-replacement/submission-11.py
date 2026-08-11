class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            Problem Approach/Notes: 
                we are going to iterate throught string s and we are going to store 
                the frequency of the characters

                We also have to track window length in order to return the max window 
                    We know that this will be some sort of sliding window problem.

                How do we know which characters to replace?
                    We can take a look at the characters that we have seen so far in our winodow 
                    and we can do a check if the characters that come up most frequency is subtracted from 
                    the window itself, we would be left with the number of replacements we would need to make 
                    in order to get the longest repeating substring 

        '''
        character_freq = {}
        longest_substr = 0
        left = 0
        window = 0

        for right in range(len(s)): 
            # we want to keep track of the freq as we keep incrementing the window
            if s[right] not in character_freq: 
                character_freq[s[right]] = 1 
            elif s[right] in character_freq: 
                character_freq[s[right]] += 1 
            
            #we need to look up the character with the highest freq and window legth 

            max_freq_val = max(character_freq.values())
            window = right - left + 1

            #now we need to check for the number of character replacements
            # if the number of character replacements is equal to k we could still be missing out on the longest window 

            while (window - max_freq_val) > k:
                character_freq[s[left]] -= 1 
                left += 1

                window = (right - left) + 1
                max_freq_val = max(list(character_freq.values()))

            longest_substr = max(window,longest_substr) 

        return longest_substr               










            


        





