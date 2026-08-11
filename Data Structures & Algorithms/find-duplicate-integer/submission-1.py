class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check_lst = []

        for i in nums:
            if i not in check_lst: 
                check_lst.append(i)
            elif i in check_lst:
                return i
        