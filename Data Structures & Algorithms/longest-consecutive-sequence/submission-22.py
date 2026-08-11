class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
    

        num_set = set(nums)

        num_set = sorted(list(num_set))
        
        print(num_set)

        counter = 1
        max_counter = 1

        for num in num_set:

            if num + 1 in num_set:
                counter += 1
            
            elif num + 1 not in num_set:
                #no longer longestConsecutive
                max_counter = max(max_counter,counter)
                counter = 1 
        
    
        return max_counter
        