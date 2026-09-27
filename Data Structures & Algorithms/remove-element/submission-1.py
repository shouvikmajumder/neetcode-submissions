class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_of_removals = 0

        while val in nums:
            nums.remove(val)
            num_of_removals +=1 
        
        return len(nums)