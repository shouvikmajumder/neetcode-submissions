class TimeMap:

    def __init__(self):
        self.timestamp = {}


    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timestamp:
            self.timestamp[key] = [[timestamp,value]]
        elif key in self.timestamp: 
            self.timestamp[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp: 
            return ""
        elif key in self.timestamp: 
            timestamp_value_lst = list(self.timestamp[key])

            if int(timestamp_value_lst[-1][0]) <= timestamp: 
                return timestamp_value_lst[-1][1]


            
            
            
        
        
