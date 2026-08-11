class Node: 
    def __init__(self,key,val):
        self.key = key 
        self.val = val

    # double linked list
        self.next = None 
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # {key,Node}

        # need to init the LL here too
        self.left,self.right = Node(0,0), Node(0,0)

        
        # make sure to link the nodes to start the double LL 
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node_before, node_after = node.prev, node.next
        node_before.next = node_after
        node_after.prev = node_before

    
    def insert(self,node): #insert node to the end of the list (right.prev!)
        self.right.prev.next = node
        
        node.prev = self.right.prev

        node.next = self.right

        self.right.prev = node 

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache: 
            newnode = Node(key,value)
            self.remove(self.cache[key])
            self.cache[key] = newnode
            self.insert(self.cache[key])
        elif key not in self.cache:
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
        
        #now we need to check if the cache is at capacity 

        if len(self.cache) > self.cap: 
            #remove LRU
            LRU = self.left.next
            self.remove(LRU)

            del self.cache[LRU.key]



            
        
        


        
