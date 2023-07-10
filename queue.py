#queue implementation using array

class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0
        
    def is_empty(self):
        return self.front == self.rear
    
    def enqueue(self, item):
        self.queue.append(item)
        self.rear += 1
        
    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(self.front)
            self.rear -= 1
        else:
            print("underflow")
        
    def size(self):
        return self.rear - self.front
    def display(self):
        if self.is_empty():
            print("queue is empty")
        else:
            for i in self.queue:
                print(i,end=" ")

obj= Queue()
obj.enqueue(3)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(5)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.display()


#queue implementation using linked list

#circular queue implementation
# class CircularQueue():

# 	# constructor
# 	def __init__(self, size): # initializing the class
# 		self.size = size
		
# 		# initializing queue with none
# 		self.queue = [None for i in range(size)]
# 		self.front = self.rear = -1

# 	def enqueue(self, data):
		
# 		# condition if queue is full
# 		if ((self.rear + 1) % self.size == self.front):
# 			print(" Queue is Full\n")
			
# 		# condition for empty queue
# 		elif (self.front == -1):
# 			self.front = 0
# 			self.rear = 0
# 			self.queue[self.rear] = data
# 		else:
			
# 			# next position of rear
# 			self.rear = (self.rear + 1) % self.size
# 			self.queue[self.rear] = data
			
# 	def dequeue(self):
# 		if (self.front == -1): # condition for empty queue
# 			print ("Queue is Empty\n")
			
# 		# condition for only one element
# 		elif (self.front == self.rear):
# 			temp=self.queue[self.front]
# 			self.front = -1
# 			self.rear = -1
# 			return temp
# 		else:
# 			temp = self.queue[self.front]
# 			self.front = (self.front + 1) % self.size
# 			return temp

# 	def display(self):
	
# 		# condition for empty queue
# 		if(self.front == -1):
# 			print ("Queue is Empty")

# 		elif (self.rear >= self.front):
# 			print("Elements in the circular queue are:",
# 											end = " ")
# 			for i in range(self.front, self.rear + 1):
# 				print(self.queue[i], end = " ")
# 			print ()

# 		else:
# 			print ("Elements in Circular Queue are:",
# 										end = " ")
# 			for i in range(self.front, self.size):
# 				print(self.queue[i], end = " ")
# 			for i in range(0, self.rear + 1):
# 				print(self.queue[i], end = " ")
# 			print ()

# 		if ((self.rear + 1) % self.size == self.front):
# 			print("Queue is Full")

# # Driver Code
# ob = CircularQueue(5)
# ob.enqueue(14)
# ob.enqueue(22)
# ob.enqueue(13)
# ob.enqueue(-6)
# ob.display()
# print ("Deleted value = ", ob.dequeue())
# print ("Deleted value = ", ob.dequeue())
# ob.display()
# ob.enqueue(9)
# ob.enqueue(20)
# ob.enqueue(5)
# ob.display()

