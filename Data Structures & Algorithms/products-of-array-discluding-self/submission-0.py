class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        zero_count = 0

        for i in nums: 
            if i == 0: 
                zero_count += 1

        if zero_count>=2:
            return [0] * len(nums)          

        elif zero_count == 1 : 
            count = 1

            for i in nums:
                if i == 0:
                    continue
                count *= i
            
            for i in nums: 
                if i == 0: 
                    out.append(count)
                else:
                    out.append(0)            
        else: 
            count = 1
            for i in nums: 
                count *= i
            
            for i in nums:
                out.append(int(count/i))        

        return out
    