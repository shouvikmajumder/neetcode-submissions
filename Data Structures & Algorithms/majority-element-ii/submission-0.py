class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        appearance_rate = len(nums)/3 
        
        freq = {}

        for num in nums:   
            if num not in freq: 
                freq[num] = 1
            elif num in freq: 
                freq[num] += 1      
        
        outputarr = []
        
        for key in freq: 
            if freq[key] > appearance_rate: 
                outputarr.append(key)
        
        return outputarr