class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = (sorted(nums))
        out = []
        for i in range(len(nums)):
            if i>0 :
                if nums[i] == nums[i-1]:
                    continue
            a = nums[i]
            l,r = i+1, len(nums) - 1

            while(l<r):
                if a + nums[l] + nums[r] == 0: 
                    if [a,nums[l],nums[r]] not in out:
                        out.append([a,nums[l],nums[r]])
                        l +=1
                        r -=1
                elif a + nums[l] + nums[r] > 0: 
                    r -=1
                elif a + nums[l] + nums[r] < 0: 
                    l += 1
        return out
                

