class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int: 
        people.sort()
        num_of_boats = 0

        left,right = 0, len(people) -1 

        while left <= right: 

            if people[left] + people[right] <= limit:
                num_of_boats += 1 
                left +=1 
                right -= 1
            elif people[left] + people[right] > limit:
                num_of_boats += 1 
                right -= 1
        return num_of_boats                

    