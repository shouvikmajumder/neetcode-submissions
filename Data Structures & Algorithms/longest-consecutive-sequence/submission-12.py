class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        print("help here", nums)
        out = []
        count = 1
        
        l, r = 0,1
        if nums == []:
            return 0
        while(r<len(nums)):
            if nums[l] + 1 == nums[r]:
                count +=1 
                l +=1 
                r +=1 
            else: 
                out.append(count)
                count = 1
                l = r 
                r += 1
            
        out.append(count)
        return max(out)