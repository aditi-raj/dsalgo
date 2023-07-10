class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def push(self, value, priority):
        new_node = Node(value, priority)

        if self.head is None:
            self.head = new_node
        elif self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def top(self):
        if self.head is None:
            return None
        else:
            return self.head.value
        
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

pq=PriorityQueue()
pq.push(4, 1)
pq.push(5, 2)
pq.push(6, 3)
pq.push(7, 0)
print(pq.top())
pq.print_list()
