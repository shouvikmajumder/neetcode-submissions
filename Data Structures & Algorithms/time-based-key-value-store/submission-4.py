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

            for value in search_lst:
                print(value)
                if value[1] <= timestamp:
                    res = value[0]
        return res
        
            



            
            