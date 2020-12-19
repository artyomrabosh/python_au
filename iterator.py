class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            node = self.head
            for i in range(index):
                node = node.next
            return node.val

    def addAtHead(self, val: int) -> None:
        cur = self.head
        new = Node(val)
        if cur is not None:
            cur.prev = new
        new.next = cur
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            new = Node(val)
            for i in range(index - 1):
                cur = cur.next
            tmp = cur
            cur = cur.next
            tmp.next = new
            new.next = cur
            new.prev = tmp
            if new.next is not None:
                new.next.prev = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        cur = self.head
        if index == 0:
            self.head = cur.next
            if cur.next is not None:
                cur.next.prev = None
        else:
            for i in range(index - 1):
                cur = cur.next
            first = cur
            second = cur.next.next
            first.next = second
            if second is not None:
                second.prev = first
        self.size -= 1

    def printList(self):
        node = self.head
        for i in range(self.size):
            print(node.val, end=" ")
            node = node.next

    def reverse(self):
        tmp = None
        cur = self.head

        while cur is not None:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev

        if tmp is not None:
            self.head = tmp.prev

class Iterator:
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration
        else:
            node = self.node
            self.node = self.node.next
            return node.val

def main():
    lst = MyLinkedList()
    lst.addAtHead(3)
    lst.addAtHead(1)
    lst.addAtTail(4)
    lst.addAtIndex(1, 2)
    lst.addAtIndex(4, 5)
    lst.deleteAtIndex(4)
    lst.printList()
    lst.reverse()
    lst.printList()

    print()

    iterator = Iterator(lst.head)
    for i in iterator:
        print(i, end=" ")


if __name__ == "__main__":
    main()