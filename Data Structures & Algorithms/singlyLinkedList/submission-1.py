class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        i = 0
        head = self.head
        while head:
            if i == index:
                return head.val
            i += 1
            head = head.next

        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def remove(self, index: int) -> bool:
        # point i - 1 next to i + 1
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        prev = self.head
        head = self.head.next
        i = 1
        while head:
            if i == index:
                next_node = head.next if head else None
                prev.next = next_node
                if head == self.tail:
                    self.tail = prev
                return True
            i += 1
            head = head.next
            prev = prev.next
        return False

    def getValues(self) -> List[int]:
        vals = []
        head = self.head
        while head:
            vals.append(head.val)
            head = head.next
        return vals

