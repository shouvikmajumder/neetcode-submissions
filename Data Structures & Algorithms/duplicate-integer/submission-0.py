class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist = []
        for i in nums:
            if i not in newlist:
                newlist.append(i)
            elif i in newlist:
                return True
        return False