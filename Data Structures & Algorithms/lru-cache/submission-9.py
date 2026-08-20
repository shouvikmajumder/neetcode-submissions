class Node:
    def __init__(self,key,value) -> None:
        # need key and value in order to properly retrieve which nodes you want to remove or get
        self.key = key 
        self.val = value

        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #this is the acutual cache

        #need a way to incorporte key and val get and put ops in O(1) ave time complexity
        self.start, self.end = Node(0,0),Node(0,0)
        self.start.next = self.end 
        self.end.prev = self.start
        #every key that gets added to the cache, we want to make sure it gets
        #added to the linked list        
    def add(self,node): 
        prev,nxt = self.end.prev, self.end 

        node.next = nxt
        prev.next = node

        node.prev = prev
        nxt.prev = node


    
    def remove(self,node):
        node_prev,  node_next = node.prev, node.next 
        node_prev.next = node_next
        node_next.prev = node_prev


    def get(self, key: int) -> int:
        #return value of the key if key exists
        if key in self.cache: 
            # remove and add back in 
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key] #node that you have to update
            self.remove(node) #remove the current node
            node.val = value
            self.add(node) #add node back in so that you know its used 
            self.cache[key] = node #update the hashmap

        elif key not in self.cache: 
            #need to add it 
            node =  Node(key,value)
            self.cache[key] = node
            self.add(node)
            #check if theres enough space otherwise remove LRU 
            if len(self.cache) > self.capacity: 
                LRU_NODE = self.start.next
                LRU_key = LRU_NODE.key
                del self.cache[LRU_key]
                self.remove(LRU_NODE)












