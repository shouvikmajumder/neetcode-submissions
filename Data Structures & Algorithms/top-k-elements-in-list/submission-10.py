class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        tracker = {}

        for num in nums: 
            
            if num not in tracker: 
                tracker[num] = 0 
            tracker[num] += 1

        outputlst = []

        tracker_val = sorted(tracker.values())[::-1]
        
        search_val = tracker_val[:k]
        
        for num in tracker:
            if tracker[num] in search_val: 
                outputlst.append(num)

        return outputlst



