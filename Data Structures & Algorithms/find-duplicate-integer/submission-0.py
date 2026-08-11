class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup_table = {}

        for i in nums: 
            if i not in dup_table: 
                dup_table[i] = 1
            elif i in dup_table: 
                return i
