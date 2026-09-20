class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.start = ListNode('dummy', None)
        self.last = self.start
        self.capacity = capacity
        self.keyToNode = {}

    def _moveToFront(self, node: ListNode):
        if self.start.next == node:
            return

        # update last node if 
        if self.last == node:
            self.last = node.prev
        elif self.last == self.start:
            self.last = node

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = self.start.next
        if self.start.next:
            self.start.next.prev = node
        self.start.next = node

    def _evict(self):
        if len(self.keyToNode) > self.capacity:
            lastKey = self.last.key
            self.last.prev.next = None
            self.last = self.last.prev
            del self.keyToNode[lastKey]

    def get(self, key: int) -> int:
        node = self.keyToNode.get(key, None)
        if not node:
            return -1

        self._moveToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        existingNode = self.keyToNode.get(key, None)
        if existingNode:
            existingNode.val = value
            self._moveToFront(existingNode)
            return

        # add to the back. call _moveToFront, then evict
        newNode = ListNode(value, key)
        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode
        self.keyToNode[key] = newNode

        self._moveToFront(newNode)
        self._evict()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
