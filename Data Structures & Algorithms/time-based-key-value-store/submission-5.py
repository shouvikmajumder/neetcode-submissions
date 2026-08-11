class TimeMap:

    def __init__(self):
        self.timesort = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timesort: 
            self.timesort[key] = [[value,timestamp]]
        elif key in self.timesort:
            self.timesort[key].append([value,timestamp])
        print(self.timesort)
    def get(self, key: str, timestamp: int) -> str:
        
        res = ""

        if key in self.timesort: 
            search_lst = list(self.timesort[key])
            
            #optimize using binary search here
            left, right = 0, len(search_lst) - 1
        
            while left <= right: 
                mp = (left + right)//2 
                
                if search_lst[mp][1] <= timestamp:
                    res = search_lst[mp][0]
                    left = mp + 1
            
                elif search_lst[mp][1] > timestamp:
                    right = mp -1 

        return res
        
            



            
            