from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colors = Counter(nums)

        overwrightlst = []

        for num in range(max(nums) + 1):
            if num in colors: 
                freq = colors[num]
                
                overwrightlst += freq *[num]

        for idx in range(len(overwrightlst)):
            nums[idx] = overwrightlst[idx]
        
        