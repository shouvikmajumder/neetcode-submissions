class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # apprach: Track index, [], total
        # two paths to take is to stay on the current index or continue on differnt path

        res = []

        stack = [(0,[],0)]

        while stack: 
            index, path, total = stack.pop()

            if total == target: 
                res.append(path)
                continue
            
            if index>= len(nums) or total > target: 
                continue
            
            # now you want to determin the exclusion and inclusion criteria
 
            stack.append((index + 1,path,total)) # move to the next value 
            stack.append((index, path + [nums[index]], total + nums[index])) #what would you do if you want to traverse a path
        
        return res