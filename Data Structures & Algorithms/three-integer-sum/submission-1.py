class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums= sorted(nums)
        out = []
        for i in range(len(sorted_nums)): 
            a = sorted_nums[i]
            templst = sorted_nums[i+1:]
            left,right = 0,len(templst)-1 
            while(left<right):
                sum = a + templst[left] + templst[right]
                if sum == 0 and [a,templst[left],templst[right]] not in out: 
                    out.append([a,templst[left],templst[right]])
                    break
                elif sum>0:
                    right -= 1
                elif sum<0: 
                    left += 1 
        return out