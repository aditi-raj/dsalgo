class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_n_node(self, n, data):
        if n == 0:
            return None
        self.head = Node(data[0])
        curr = self.head
        if n == 1:
            return curr
        for i in range(1, n):
            new = Node(data[i])
            curr.next = new
            curr = new
#this is traverse 
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val,end=" ")
            temp = temp.next

    def insert_node_sorted(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        if data < self.head.val:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None and curr.next.val < data:
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

    def delete_node(self, val):
        if self.head is None:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next is not None and curr.next.val != val:
            curr = curr.next

        if curr.next is None:
            return

        curr.next = curr.next.next

train = LinkedList()
train.create_n_node(4, [2,6,9,10])
train.insert_node_sorted(4)
train.delete_node(9)
train.printList()
