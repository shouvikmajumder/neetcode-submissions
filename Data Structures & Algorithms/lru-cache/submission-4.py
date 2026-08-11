class Node: 
    def __init__(self,key,val) -> None:
        self.key = key
        self.val = val 
        
        self.next = None 
        self.prev = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head_node, self.tail_node = Node(0,0), Node(0,0)

        #now you have to setup the DLL
        self.head_node.next = self.tail_node #dont have to change prev since its already None
        self.tail_node.prev = self.head_node # dont have to change next since its already None

    def add(self,node):
        # add it to the end
        prev_node = self.tail_node.prev
        
        temp = prev_node.next #connection to the tail node
        prev_node.next = node 
        node.next = temp
        node.prev = prev_node
        self.tail_node.prev = node
        
    def remove(self,node):
        curr = self.head_node
        
        while curr:
            if curr == node: 
                prev_node = curr.prev
                next_node = curr.next
                
                prev_node.next = next_node
                next_node.prev = prev_node
            curr = curr.next    

    def get(self, key: int) -> int:
        if key in self.cache:
            #remove and add it back into the linkedlist
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache: 
            old_node = self.cache[key]
            new_node = Node(key,value)            
            self.remove(old_node)
            self.add(new_node)

            self.cache[key] = new_node

        elif key not in self.cache: 
            #means you have to add it 
            new_node = Node(key,value)
            self.cache[key] = new_node 
            # need to check size
            if len(self.cache) > self.capacity: 
                #remove the node to the right of head which is LRU
                lru_node = self.head_node.next
                lru_key = lru_node.key
                del self.cache[lru_key]
                self.remove(lru_node)
                # need to delete the key from the cache
                

'''
----Notes----
 
- How to create a DLL :
    node1<-->node2 -->

- cache is going to DLL (need to init a Node class)
    self.cache is going to be the actual cache: 
        -DLL is just going to serve as a way to detect LRU

- need 2 helper functions (remove and add)

funtion remove: remove a specefic node from the DLL
function add: add a node to the end of a linkedlist


func put either add or updates
    - therefore whenever you have to add you also need to check the size
    - if the size > capacity: remove the node at the beginning of the DLL
 
func get
    - if the key is in the DLL, then you have delete that node and  
    add it to the end of the DLL 



'''

