import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''ForwardRef, 
        We are going to involve some kind of frequency table to keep track of the list 

        need a heap and pop from it untill the len of the heap is == to k.
         
        How to determine what is going to go into the heap it is dependent on the frequecy 

        we can put the freq values and initialzie that as the heap
        
        then we can iterate throught that heap to see which keys correspond to the values
        '''

        freq_table = {}
        
        for num in nums: 
            if num not in freq_table:
                freq_table[num] = 1
            elif num in freq_table:
                freq_table[num] +=1

        min_heap = list(freq_table.values())

        heapq.heapify(min_heap) 

        while len(min_heap) > k:
            heapq.heappop(min_heap)


        k_most_freq = []

        
        for key in freq_table: 
            if freq_table[key] in min_heap: 
                k_most_freq.append(key)

        return k_most_freq
