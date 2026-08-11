class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []

        for i in nums:
            if i not in lst:
                lst.append(i)
            elif i in lst:
                return True 
        return False
        


         