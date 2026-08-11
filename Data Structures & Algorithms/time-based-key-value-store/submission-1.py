class TimeMap:

    def __init__(self):
        self.key_value_store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.key_value_store: 
            self.key_value_store[key] = [value,timestamp]
        elif key in self.key_value_store:
            self.key_value_store[key][0] = value
            self.key_value_store[key][1] = timestamp
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.key_value_store and self.key_value_store[key][1] <= timestamp: 
            return self.key_value_store[key][0]
        else: 
            return ""
        

        
