# Evict by LFU then LRU
"""
track LFU and when operated on, check for new LFU this is a draw.
also when evicted and inserted new key is LFU unless draw, as it MRU

frq to LRU keys
keys to nodes directly
poiunter to LFU and LRU, for O(1) evict on put, then u update newley added key as as first to evict or check map for 1 and get oldest one there.
we should have pointer to start and end of list


get -> update freq, we have map to node, move it freq bucket at start or create new bucket
put -> putting existing key is the same as get but we dont care about the value

putting new key ->
    evict node if needed, then insert new node and talk and update LFU pointer ->
        its either new added node as freq == 1 or check freq 1 list and choose last one

"""

class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1
        self.key = key

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currCap = 0
        self.freqMap = {}
        self.kvMap = {}
        self.nextEvict = None

    def get(self, key: int) -> int:
        if key not in self.kvMap:
            return -1
        
        node = self.kvMap[key]
        # update prev freq map
        if node.prev and node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
        elif not node.next and not node.prev:
            # only node in bucket
            del self.freqMap[node.freq]
        elif not node.next:
            # last node
            newEnd = node.prev
            newEnd.next = None
            startNode, _ = self.freqMap[node.freq]
            self.freqMap[node.freq] = (startNode, newEnd)
        else:
            # start node
            newStart = node.next
            newStart.prev = None
            _, endNode = self.freqMap[node.freq]
            self.freqMap[node.freq] = (newStart, endNode)

        # update new freq bucket
        node.freq += 1
        if node.freq in self.freqMap:
            prevStartNode, endNode = self.freqMap[node.freq]
            prevStartNode.prev = node
            node.next = prevStartNode
            self.freqMap[node.freq] = (node, endNode)
        else:
            # MRU, LRU
            self.freqMap[node.freq] = (node, node)

        # update Last evict
        if self.nextEvict == node:
            if node.freq - 1 in self.freqMap:
                _, self.nextEvict = self.freqMap[node.freq - 1]
            else:
                _, nextEvict = self.freqMap[node.freq]
                self.nextEvict = nextEvict
        
        return node.val

    def put(self, key: int, value: int) -> None:
        # update value case
        if key in self.kvMap:
            node = self.kvMap[key]
            node.val = value
            self.get(key)
            return
        
        newEntry = ListNode(key, value)

        # deal with first entry case
        if self.nextEvict == None:
            self.nextEvict = newEntry
            self.freqMap[1] = (newEntry, newEntry)
            self.currCap += 1
            self.kvMap[key] = newEntry
            return

        if self.currCap == self.capacity:
            # delete from freq bucket
            node = self.nextEvict
            self.currCap -= 1

            # can only delete the last node in a bucket as it is LRU
            if not node.next and not node.prev:
                # will assign
                del self.freqMap[node.freq]
                self.nextEvict = None
            elif not node.next:
                startNode, currLast = self.freqMap[node.freq]
                newLast = currLast.prev
                newLast.next = None
                self.nextEvict = newLast
                self.freqMap[node.freq] = (startNode, newLast)

            del self.kvMap[node.key]

        self.currCap += 1
        self.kvMap[key] = newEntry
        if 1 in self.freqMap:
            currFirst, lastNode = self.freqMap[1]
            newEntry.next = currFirst
            currFirst.prev = newEntry
            self.freqMap[1] = (newEntry, lastNode)
        else:
            self.nextEvict = newEntry
            self.freqMap[1] = (newEntry, newEntry)
        







        

        








# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)