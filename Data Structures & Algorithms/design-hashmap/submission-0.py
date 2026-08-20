class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        # insert a key value pair into the hashmap
        # however if the kjey is alreayd in the map, update the value
        
        if key in self.hashmap:
            self.hashmap[key] = value
        self.hashmap[key] = value


    def get(self, key: int) -> int:
        # return the value of the key if the key doesnt exist return -1
        if key not in self.hashmap: 
            return -1 
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        # if they key in the map remove it
        if key in self.hashmap:
            del self.hashmap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)