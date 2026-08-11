class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        
        for i in nums: 
            if i not in check:
                check.append(i)
            elif i in check: 
                return True 
        return False


         