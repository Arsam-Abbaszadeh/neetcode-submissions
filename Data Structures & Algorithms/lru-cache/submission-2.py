class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv = {}
        self.last = None
        self.first = None

    def get(self, key: int) -> int:
        node = self.kv.get(key)
        if not node:
            return -1
        
        if self.first != node:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.last = node.prev

            node.prev = None
            node.next = self.first
            self.first.prev = node
            self.first = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            node = self.kv[key]
            node.val = value

            if self.first.key != key:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.last = node.prev

                node.prev = None
                node.next = self.first
                self.first.prev = node
                self.first = node      
        else:
            # add to list
            node = Node(key, value) 
            node.next = self.first
            if self.first:
                self.first.prev = node
            else:
                self.last = node
            self.first = node
            self.kv[key] = node
            # remove extra if overflow
            if len(self.kv) > self.capacity:
                node = self.last
                del self.kv[node.key]
                self.last = node.prev
                if self.last:
                    self.last.next = None
                else:
                    self.first = None


