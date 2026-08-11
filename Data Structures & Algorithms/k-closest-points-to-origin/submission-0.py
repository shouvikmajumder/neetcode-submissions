from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
            Using a heap here is best 

            You can go through every coordinate pair and store it in a list as dist x and y 

            when you heapify the list the first element becomes the smalles so when you heapop

            you can then append the coordinate pair to a list k times, which would end up getting you the 

            k closet coordinate pairs
        '''
        
        minHeap = []

        for x,y in points: 
            dist = ((x ** 2) + (y ** 2)) ** (1/2)
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap)

        print(minHeap)
        # now that its sorted properly we jus need to append the closest vals k times to an output

        res = []

        while k > 0:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1        

        return res




