class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        num_lst = list(nums_set)
        
        num_lst.sort()

        print(num_lst)
        left = 0
        counter = 1
        max_counter = 0

        if len(num_lst) == 0: 
            return 0 
        
        elif len(num_lst) == 1: 
            return 1 

        else: 
            for right in range(1,len(num_lst)):
                if num_lst[right] - num_lst[left] == 1: 
                    counter += 1
                
                elif num_lst[right] - num_lst[left] != 1: 
                     counter = 1
                     max_counter = max(counter,max_counter)
                max_counter = max(counter,max_counter)
                left += 1
                print(max_counter)

            max_counter = max(counter,max_counter)
        return max_counter

                




