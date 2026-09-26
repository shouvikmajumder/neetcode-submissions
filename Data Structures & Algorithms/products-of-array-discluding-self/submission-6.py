class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # we need a prefix array and a postfix array
        # mulitply both outpcomes into an ouput lst 

        prefix_lst = [1] * len(nums)
        suffix_lst = [1] * len(nums)

        output = [1] * len(nums)

        curr_pre = 1
        for i in range(len(nums)):  
            prefix_lst[i] = curr_pre
            curr_pre *= nums[i]
        curr_suff = 1
        for i in range(len(nums)-1, -1, -1): 
            suffix_lst[i] = curr_suff
            curr_suff *= nums[i]

        for i in range(len(nums)):
            output[i] = prefix_lst[i] * suffix_lst[i]

        return output