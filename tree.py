class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
    
    def insert(self,data):
        if self.value<data:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)
        elif self.value>data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_node = self.right
            while min_node.left:
                min_node = min_node.left
            self.value = min_node.value
            self.right = self.right.delete(min_node.value)
        return self
        
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value,end=' ')
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.value,end=' ')
        
    def bfs(self,root):
        q=[]
        all_nodes=[]
        q.append(root)
        while q:
            node=q.pop(0)
            all_nodes.append(node)
            if node.left and node.left not in all_nodes:
                q.append(node.left)
            if node.right and node.right not in all_nodes:
                q.append(node.right)
        
        for node in all_nodes:
            print(node.value,end=" ")

    def top(self,root):
        if root:
            return root.value
    def bottom(self,root):
        if root:
            temp=root
            while temp.left:
                temp=temp.left
        return temp.value
    

            


root=Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(14)
root.insert(4)
root.insert(7)
root.insert(13)
# root.inorder(root)
root.delete(14)
root.delete(6)
# print(root.bottom(root))
# root.inorder(root)
root.bfs(root)


