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
        else: 

            counter = 1
            num_set = set(nums)            
            num_lst = list(num_set)
            num_lst.sort()

            max_counter = 1

            for num in num_lst: 

                if num + 1 in num_set: 
                    counter += 1
                
                elif num + 1 not in num_set: 
                    max_counter = max(max_counter,counter)
                    counter =  1

            return max_counter


                        


            








