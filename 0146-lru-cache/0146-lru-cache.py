"""
WE need order for the keys based on recents
We have an LRU with dictionary where it maps key to number of times called
We keep track of a LRU single value

We use a doubly linkedlist to keep track of lru

We do dictionary where key: [Node, value]

For the get() method
    We disconnect one node and move it to the front
    If we change the last element we have to update it 

For the put() method
    If len(dict)==capacity:
        We remove last connection and create new connection where new_node is at front

"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        #We use head and tail for less edge cases
        self.tail = Node(0,0)
        self.head = Node(0,0)

        self.tail.next = self.head
        self.head.prev = self.tail
    
    def remove(self,node: Node):
        prev_node = node.prev
        next_node = node.next

        next_node.prev = prev_node
        prev_node.next = next_node

    def add_head(self,node: Node):
        curr_head = self.head.prev
        curr_head.next = node
        node.prev = curr_head
        node.next = self.head
        self.head.prev = node


    def get(self, key: int) -> int:
        #Case where it is not in keys
        if key not in self.keys:
            return -1
        #Case where it is in
        else:
            #if it is head
            if self.keys[key][0]==self.head.prev:
                return self.keys[key][1]
            #other cases
            self.remove(self.keys[key][0])
            self.add_head(self.keys[key][0])

            return self.keys[key][1]
        

    def put(self, key: int, value: int) -> None:
        new_node = Node(key,value)
        

        if key in self.keys:
            self.remove(self.keys[key][0])
            self.keys[key] = [new_node,value]
            self.add_head(self.keys[key][0])
            return
        elif len(self.keys)>=self.capacity:
            self.keys[key] = [new_node,value]
            del self.keys[self.tail.next.key]
            self.remove(self.tail.next)
            self.add_head(new_node)
            return
        else:
            self.keys[key] = [new_node,value]
            self.add_head(new_node)








        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)