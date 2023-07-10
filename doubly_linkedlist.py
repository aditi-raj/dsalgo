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
    
    def insert_at_beg(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            self.head=new_node
            new_node.next=curr
            curr.prev=new_node
    
    def insert_inbtw(self,data,key):
        new_node=Node(data)
        if not self.head:
            print("key is not present")
        key_node=self.head
        while key_node.val!=key:
            key_node=key_node.next
        next_node=key_node.next
        key_node.next=new_node
        new_node.prev=key_node
        next_node.prev=new_node
        new_node.next=next_node

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
    def del_beg(self):
        if not self.head:
            print("list is empty")
        else:
            next_node=self.head.next
            self.head=next_node
            next_node.prev=None
    
    def del_end(self):
        last=self.head

        while last.next is not None:
            last=last.next
        curr=last.prev
        last.prev=None
        curr.next=None


    def traverse_forward(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next
        print()

    def traverse_backward(self):
        last=self.head
        while last.next is not None:
            last=last.next
        while last.prev is not None:
            print(last.val,end=" ")
            last=last.prev
        print(last.val)

train = DoublyLinkedList()
train.insert_node(2)
train.insert_node(5)
train.insert_node(3)
train.insert_at_beg(10)
train.insert_inbtw(9,5)
train.traverse_forward()  # Output: 10 2 5 9 3 
train.traverse_backward() #Output: 3 9 5 2 10
# train.delete_node(3)
train.del_beg()
train.del_end()
train.traverse_forward() # Output: 2 5 9 
train.traverse_backward() #OuTPUT 9 5 2
