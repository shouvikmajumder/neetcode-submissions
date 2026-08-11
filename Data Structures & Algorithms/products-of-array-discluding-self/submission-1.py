class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []

        zero_count = 0

        for i in nums: 
            if i == 0:
                zero_count +=1

        if zero_count>=2:
            return len(nums) * [0]

        elif zero_count == 0: 
            total = 1
            for i in nums: 
                total *= i
            lst = []
            for i in nums: 
                lst.append(int(total/i))
            return lst
        
            
        elif zero_count == 1:
            #[42,12,0,2]
            total = 1
            for i in nums:
                if i != 0: 
                    total *= i
            lst =[]
            for i in nums: 
                if i != 0:
                    lst.append(0)
                elif i == 0: 
                    lst.append(int(total))
            return lst
    



