class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplst = []

        for i in nums:
            if i in duplst:
                return True 
            elif i not in duplst:
                duplst.append(i)
        return False