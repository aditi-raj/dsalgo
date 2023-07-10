class Node:
    def __init__(self, data):
        self.val = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr

    def delete_node(self, data):
        curr = self.head

        while curr is not None:
            if curr.val == data:
                if curr.prev is None:
                    self.head = curr.next
                    if curr.next is not None:
                        curr.next.prev = None
                else:
                    curr.prev.next = curr.next
                    if curr.next is not None:
                        curr.next.prev = curr.prev

                return

            curr = curr.next

    def traverse(self):
        curr = self.head

        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next

        print()

train = DoublyLinkedList()
train.insert_node(2)
train.insert_node(5)
train.insert_node(3)
train.insert_node(5)
train.insert_node(6)
train.traverse()  # Output: 2 5 3 5 6
train.delete_node(3)
train.traverse()  # Output: 2 5 5 6
