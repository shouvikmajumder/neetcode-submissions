class TimeMap:

    def __init__(self):
        self.timestamp = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
            self.timestamp[key] = [timestamp,value]


    def get(self, key: str, timestamp: int) -> str:
        for i in self.timestamp: 
            time_stamp_time, time_stamp_value = self.timestamp[i][0], self.timestamp[i][1]

            if i == key and time_stamp_time <= timestamp:
                return time_stamp_value

        return ""
            
            
            
        
        
