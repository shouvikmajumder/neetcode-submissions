import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        ''' 
            The ideal way to solve this problem is to use a maxHeap and a queue 

                You would essentially store the frequencies of all of the differen chars in a dict
                where you can use that dict to build a maxHeap 

                The heap is going to contain 2 objects in an item (char freq, time)
                    this is because you are able to determine if run the process again once the cooldown 
                    time is met 

                At some point you are going to run out of cpu processes and the way to handle that is 
                see if there is anything left in the queue or heap in general 

                Initally the queue is not going to have any processes and once the heap runs out of processes
                you make the time whatever is left in the queue as it would be the last process


                Small things: 
                    make sure that you handle the case when the count becomes 0, because you already ran all of the processes
        '''

        task_count = Counter(tasks)
        maxHeap = [-1 * task for task in list(task_count.values())]

        heapq.heapify(maxHeap)
        
        queue = deque()
        time = 0

        while maxHeap or queue: #this is basically saying that while there still is process running
            time += 1 

            if not maxHeap: 
                time = queue[0][1] # (task_freq,time) 
            #if there are still processes in the maxHeap we want to pop it out increment the time + n and put it into the queue
            else: 
                        
                count = heapq.heappop(maxHeap) + 1 # since this counts as a useage we an decrement 

                if count: 
                    queue.append([count, time + n]) # time + n is the next time you are able to use this process again 

            if queue and queue[0][1] == time: 
                # if the current time matches thet time of the heap the cooldown is set so you can push freq back into the list
                count,time = queue.popleft() 
                heapq.heappush(maxHeap,count)
            

        return time










