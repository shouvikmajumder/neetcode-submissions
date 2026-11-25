class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_sum_arr = [1] * len(nums)
        suffix_sum_arr = [1] * len(nums)

        forward_counter = 1 
        backward_counter = 1
        for idx in range(len(nums)):
            prefix_sum_arr[idx] = forward_counter    
            forward_counter *= nums[idx]

        for idx in range(len(nums)-1, -1, -1):
            suffix_sum_arr[idx] = backward_counter
            backward_counter *= nums[idx]
    
        return [prefix_sum_arr[idx] * suffix_sum_arr[idx] for idx in range(len(nums))]