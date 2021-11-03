import unittest

class Node:
    def __init__(self, value = None) -> None:
        self.next = None
        self.val = value

class SLinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

    def add(self, val):
        if not self.__head:
            self.__head = Node(val)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(val)
            self.__tail = self.__tail.next

    def removeByVal(self, val):
        head = self.__head
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
    
    def removeByPos(self, pos):
        if pos < 1:
            return False
        
        if pos == 1:
            return self.removeHead()
        
        head = self.__head
        prev = None
        while head and pos > 1:
            if pos == 1:
                prev.next = head.next
                return head.val
            else:
                pos -= 1
                prev = head
                head = head.next
            
        return -1
                

    def removeHead(self):
        if self.__head and self.__tail == self.__head:
            self.__head = self.__head.next
            self.__head = self.__head
        elif self.__head:
            self.__head = self.__head.next
        else:
            return False
        
        return True
    
    def toArray(self):
        arr = []
        head = self.__head
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

class TestLinkedList(unittest.TestCase):
    def test_initialization(self):
        ls = SLinkedList()
        self.assertEqual(ls.toArray(), [])
        self.assertEqual(ls.head(), None)
        self.assertEqual(ls.tail(), None)

    def test_add(self):
        ls = SLinkedList()
        ls.add(1)
        ls.add(2)
        ls.add(3)
        self.assertEqual(ls.head().val, 1)
        print(ls.toArray())
        self.assertEqual(ls.tail().val, 3)

if __name__=='__main__':
    unittest.main()