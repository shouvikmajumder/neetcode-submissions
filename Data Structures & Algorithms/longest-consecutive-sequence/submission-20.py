class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        num_lst = list(nums_set)

        print(num_lst)
        counter = 1
        max_counter = 0

        if len(num_lst) == 0: 
            return 0 
        
        elif len(num_lst) == 1: 
            return 1 

        else: 

            for i in range(len(num_lst)):
                value = num_lst[i]

                if value + 1 in nums_set:
                    counter +=1
                    max_counter = max(counter,max_counter)
                
                elif value + 1 not in nums_set: 
                    max_counter = max(counter,max_counter)
                    counter = 1 
                

            max_counter = max(counter,max_counter)
        return max_counter

                




