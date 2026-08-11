import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        maxHeap --> flip the weights of the stones and turn it into a "maxHeap" 
        while len(maxHeao) > 1 : we want to evaluate x and y or keep popping elements out of the List
        or at least untill list size becomes 1 

        At the end we should have a maxHeap[0] to return which would be the final stone
        '''
        
        if len(stones) == 1: 
            return stones[0] #return the weight of just that 1 stone

        
        flip_weights = [ -1 * num for num in stones]

        heapq.heapify(flip_weights)

        while len(flip_weights) > 1: 
            y,x = heapq.heappop(flip_weights), heapq.heappop(flip_weights)
            
            # now you want to run throught the conditions
            if abs(x) < abs(y):
                y = abs(y) - abs(x)
                heapq.heappush(flip_weights, -1 * y)
 
            elif abs(y)> abs(x):
                #push them back into the heap
                heapq.heappush(flip_weights,y)  
                heapq.heappush(flip_weights,x)
        
        if len(flip_weights) == 0 : 
            return 0

        return abs(flip_weights[0])  
