class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        unique_quads = []
        for a in range(len(nums)-3):

            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a + 1,len(nums) - 2):
                left, right = b + 1, len(nums) - 1

                while left < right:

                    if nums[a] + nums[b] + nums[left] + nums[right] == target: 
                        unique_quads.append([nums[a],nums[b],nums[left],nums[right]])
                        left +=1
                        right -= 1 
                    elif nums[a] + nums[b] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[a] + nums[b] + nums[left] + nums[right] < target:
                        left += 1 
        return unique_quads