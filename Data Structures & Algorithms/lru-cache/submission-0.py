class Node: 
    
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #map key to Node
        self.cache = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            previous = node.prev
            after = node.next
            previous.next = after
            after.prev = previous

            last = self.right.prev
            last.next = node
            node.prev = last
            node.next = self.right
            self.right.prev = node
            
            

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache: 
            node = self.cache[key]
            previous = node.prev
            after = node.next
            previous.next = after
            after.prev = previous

        node = Node(key, value)
        self.cache[key] = node
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node
        
        if len(self.cache) > self.capacity: 
            lru = self.left.next
            after = lru.next
            self.left.next = after
            after.prev = self.left
            del self.cache[lru.key]









        
