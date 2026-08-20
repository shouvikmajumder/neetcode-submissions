class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        # insert the value key in to the hashet
        self.hashset.append(key)

    def remove(self, key: int) -> None:
        #if the key is in the hashset you remove it, otherwise do nothing
        while key in self.hashset: 
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)