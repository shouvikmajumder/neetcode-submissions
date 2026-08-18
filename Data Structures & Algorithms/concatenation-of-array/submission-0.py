class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy_lst = nums.copy()
        
        output = nums + copy_lst
        
        return output 