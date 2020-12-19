import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self, num):
        self.len = len(num)
        a = Node(num[0])
        self.head = a
        for i in range(1, len(num)):
            a.next = Node(num[i])
            a = a.next

    def convert(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        a = self.head
        for i in range(self.len):
            if a.val in letters:
                a.val = 10 + letters.index(a.val)
            else:
                a.val = int(a.val)
            a = a.next
        return self

    def reconvert(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        a = self.head
        for i in range(self.len):
            if a.val > 9:
                a.val = letters[a.val - 10]
            a = a.next
        return self

    def add(self, second):
        self = self.convert()
        second = second.convert()
        if self.len < second.len:
            first = second
            second = self
        else:
            first = self
        len = second.len
        a = first
        first = first.head
        second = second.head
        for i in range(len):
            if first.val + second.val <= 15:
                first.val = first.val + second.val
            else:
                sum = first.val + second.val
                sum -= 16
                if i is (a.len - 1):
                    A = Node(0)
                    first.next = A
                    a.len += 1
                first.next.val += 1
                if first.next.val >= 16:
                    x = first.next
                    while x.val >= 16:
                        x.val -= 16
                        if x.next is None:
                            x.next = Node(0)
                            a.len += 1
                        x.next.val += 1
                        x = x.next
                first.val = sum
            first = first.next
            second = second.next

        a = a.reconvert()
        return a

    def __str__(self):
        res = ""
        a = self.head
        for i in range(self.len):
            a.val = str(a.val)
            res = res + a.val
            a = a.next
        res = res[::-1]
        return res



def do(first, second):
    second = second[::-1]
    first = first[:: -1]
    first = LinkedList(first)
    second = LinkedList(second)

    first = first.add(second)

    print(first)




if __name__ == '__main__':
    hexnumber = sys.argv
    do(hexnumber[1], hexnumber[2])