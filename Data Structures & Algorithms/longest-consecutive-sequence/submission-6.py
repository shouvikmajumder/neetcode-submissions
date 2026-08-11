class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = []

        l,r = 0,1

        nums = sorted(set(nums))
        lst = []

        while(r<=len(nums)-1):
            if nums[l]+1 == nums[r] or nums[l] == nums[r]:
                if l == 0 :
                    lst.append(nums[l]) 
                lst.append(nums[r])
                r += 1
            else:
                out.append(lst)
                l +=1 
                r = l + 1
        output = 0 
        prev = 0
        
        for i in out:
            if len(i)>prev:
                prev = len(i)
                output = i 
        
        return int(len(output))

        