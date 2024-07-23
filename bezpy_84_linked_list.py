class ListNode:
    'A single node of a singly linked list'
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    'A Linked List class'
    def __init__(self):
        self.head = None

    def insert(self, data):
        'insertion method for the linked list'
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = ListNode(data)
        else:
            self.head = ListNode(data)

    def print_list(self):
        'print method for the linked list'
        current = self.head
        while (current):
            print(current.data, end=' -> ')
            current = current.next
        print()

    def count_list(self):
        'print method for the linked list'
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        print(counter)


    def ll_to_list(self):
        'Returns a python list from a linked list'
        digits = []
        current = self.head
        while current:
            digits.append(current.data)
            current = current.next
        return digits


    @staticmethod
    def list_to_ll(l):
        ll = LinkedList()
        for n in l:
            ll.insert(n)
        return ll

# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert('a')
LL.insert('b')
LL.insert('c')
LL.count_list()
LL.print_list()
print(LL.ll_to_list())

LL2 = LinkedList.list_to_ll([1,2,3])
LL2.print_list()