class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node   

    def pop(self) -> int:
        if not self.tail:
            return -1
        
        value = self.tail.val
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        return value        

    def popleft(self) -> int:
        if not self.head:
            return -1

        value = self.head.val
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        return value