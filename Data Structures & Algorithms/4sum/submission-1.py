class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        quads = []
        for a in range(len(nums)-3):

            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a + 1,len(nums) - 2):
                
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                left, right = b + 1, len(nums) - 1
                
                while left < right:
                    subarr = [nums[a],nums[b],nums[left],nums[right]]
                    if nums[a] + nums[b] + nums[left] + nums[right] == target:
                        quads.append(subarr)
                        left +=1
                        right -= 1 

                        while left < right and nums[left] == nums[left -1]:
                            left += 1

                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1

                    elif nums[a] + nums[b] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[a] + nums[b] + nums[left] + nums[right] < target:
                        left += 1   
        return quads