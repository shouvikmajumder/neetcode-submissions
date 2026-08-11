class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums= sorted(nums)
        out = []
        for i in range(len(sorted_nums)): 
            a = sorted_nums[i]
            left,right = i+1,len(sorted_nums)-1 
            while(left<right):
                sum = a + sorted_nums[left] + sorted_nums[right]
                if sum == 0 and [a,sorted_nums[left],sorted_nums[right]] not in out: 
                    out.append([a,sorted_nums[left],sorted_nums[right]])
                    break
                elif sum>0:
                    right -= 1
                elif sum<0: 
                    left += 1 
        return out
                    
                    