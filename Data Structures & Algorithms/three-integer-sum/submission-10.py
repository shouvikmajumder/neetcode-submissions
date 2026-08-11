class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-2-3,,-1,0,1,2,3]
        # out [0,3,6], [-2,-1,3]
        # sort nums
        # itr thru nums 
        # on every iteration use 2 ptrs
        # if there is a sum == 0 append to out
        # l+=1, r-=1, since l==r not yet 
        # 
        # if sum>0 move r -=1
        # if sum<0 move l +=1 

        out = []
        nums = sorted(nums)
        print(nums)

        for i in range(len(nums)):
            l,r = i + 1, len(nums)-1 

            while(l<r):
                if nums[i] + nums[l] + nums[r] == 0 :
                    if [nums[i],nums[l],nums[r]] not in out: 
                        out.append([nums[i],nums[l],nums[r]])
                    l +=1 
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l +=1 
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1 
            
        return out

