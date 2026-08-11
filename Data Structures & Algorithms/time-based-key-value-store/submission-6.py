class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map: 
            self.time_map[key] = [[value, timestamp]]
        elif key in self.time_map: 
            self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""

        if key in self.time_map: 

            search_lst = self.time_map[key] 
            print(type(search_lst))
            
            left, right = 0, len(search_lst) -1 

            while left <= right: 
                mid_p = (left + right) // 2 

                val, time = search_lst[mid_p][0],search_lst[mid_p][1]

                if time <= timestamp: 
                    res = val
                    left = mid_p + 1
                elif time > timestamp: 
                    right = mid_p - 1
                    
        return res

                



        return res 
        