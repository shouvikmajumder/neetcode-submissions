class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup_lst = []

        for i in nums: 
            if i in dup_lst: 
                return True
            dup_lst.append(i)
        return False