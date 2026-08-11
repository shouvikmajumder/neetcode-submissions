class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Problem Approach/Notes: 
                Sort the input array, we can iterate throught the array to make it a set, which contains
                unique nums that are orderred

                have a currCounter to count the current instance and a maxCounter to track the
                longestConsecutive sequnce that we have seenn so far 

                iterate throught nums and if there is a nums + 1 in the set, increment the coutner 
                if nums + 1 not in set you set the curre coutner to the maxCounter and start counting from 0 again                 
        '''
        if len(nums) == 0: 
            return 0
        elif len(nums) == 1:
            return 1

        nums_set = set(nums)        
        nums = list(nums_set)
        nums.sort()

        counter = 1 
        max_Counter = 1

        for num in nums:
            print(num)
            # print(counter)
            if (num + 1) in nums_set: 
                counter += 1
            elif (num + 1) not in nums_set:
                counter = 1
            
            max_Counter = max(max_Counter,counter)

        return max_Counter






