class ListNode:
    def __init__(self, key=None, val=None):
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1
        self.key = key


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()   # dummy MRU-side node
        self.tail = ListNode()   # dummy LRU-side node

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self):
        return self.head.next == self.tail

    def addFirst(self, node):
        # insert directly after dummy head = MRU
        first = self.head.next

        node.prev = self.head
        node.next = first

        self.head.next = node
        first.prev = node

    def remove(self, node):
        # works for middle, first, last, only real node
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

    def getLast(self):
        if self.isEmpty():
            return None

        return self.tail.prev


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currCap = 0

        # freq -> DoublyLinkedList
        self.freqMap = {}

        # key -> ListNode
        self.kvMap = {}

        self.nextEvict = None

    def get(self, key: int) -> int:
        if key not in self.kvMap:
            return -1

        node = self.kvMap[key]
        oldFreq = node.freq

        oldList = self.freqMap[oldFreq]

        # No more:
        #
        # if node.prev and node.next:
        # elif not node.next and not node.prev:
        # elif not node.next:
        # else:
        #
        # Dummy nodes mean removal is always identical.
        oldList.remove(node)

        if oldList.isEmpty():
            del self.freqMap[oldFreq]

        # move to next frequency
        node.freq += 1

        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DoublyLinkedList()

        # newly accessed node becomes MRU in new frequency bucket
        self.freqMap[node.freq].addFirst(node)

        # update next eviction node
        if self.nextEvict == node:
            # If old frequency bucket still exists, its LRU is next eviction
            if oldFreq in self.freqMap:
                self.nextEvict = self.freqMap[oldFreq].getLast()

            else:
                # old LFU bucket disappeared, so this node's new bucket
                # is now the minimum frequency bucket
                self.nextEvict = self.freqMap[node.freq].getLast()

        return node.val

    def put(self, key: int, value: int) -> None:
        # existing key
        if key in self.kvMap:
            node = self.kvMap[key]
            node.val = value

            # updating existing key counts as access
            self.get(key)
            return

        newEntry = ListNode(key, value)

        # first entry
        if self.nextEvict is None:
            self.freqMap[1] = DoublyLinkedList()
            self.freqMap[1].addFirst(newEntry)

            self.nextEvict = newEntry
            self.currCap += 1
            self.kvMap[key] = newEntry
            return

        # cache full: evict LFU, then LRU among that frequency
        if self.currCap == self.capacity:
            node = self.nextEvict
            freq = node.freq

            freqList = self.freqMap[freq]

            # Again: no head/tail/only-node conditionals
            freqList.remove(node)

            if freqList.isEmpty():
                del self.freqMap[freq]
                self.nextEvict = None
            else:
                self.nextEvict = freqList.getLast()

            del self.kvMap[node.key]

            self.currCap -= 1

        # insert new key with frequency 1
        self.currCap += 1
        self.kvMap[key] = newEntry

        if 1 not in self.freqMap:
            self.freqMap[1] = DoublyLinkedList()

        self.freqMap[1].addFirst(newEntry)

        # Any new node has frequency 1, therefore frequency 1 is LFU.
        # The eviction candidate is the LRU node in that bucket.
        self.nextEvict = self.freqMap[1].getLast()