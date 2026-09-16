class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights), sum(weights)
        least_weight_cap = 1000000


        def calc_days(weight_cap): 
            days_req = 1
            counter = 0

            for weight in weights: 
                if counter + weight > weight_cap:
                    days_req +=1 
                    counter = 0 
                counter += weight 
            print(days_req)
            return days_req   

        while left <= right:
            weight_cap = (left + right) // 2 
            days_calc = calc_days(weight_cap)

            if days_calc <= days:
                least_weight_cap = min(least_weight_cap,weight_cap)
                right = weight_cap - 1 
            else:
                left = weight_cap + 1
                
        return least_weight_cap