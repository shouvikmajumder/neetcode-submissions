class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #need a prefix array and a suffix array then multiply them together

        prefix_arr = [1] * len(nums)
        postfix_arr = [1] * len(nums)

        temp = 1 

        for i in range(len(nums)):
            prefix_arr[i] = temp
            temp *= nums[i]

        temp = 1
        for i in range(len(nums)-1, -1 ,-1):
            postfix_arr[i] = temp
            temp *= nums[i]

        return [prefix_arr[i] * postfix_arr[i] for i in range(len(nums))]


            