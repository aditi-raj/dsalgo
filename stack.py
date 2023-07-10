class Stack:
    def __init__(self):
        self.stack = []  # initialize an empty stack
        self.size = 0    # set the initial size to 0
    
    def push(self, element):
        self.stack.append(element)
        self.size += 1
    
    def isempty(self):
        return self.size == 0

    def pop(self):
        if self.isempty():
            return None  # return None instead of 0 if stack is empty
        else:
            
            self.size -= 1
            return self.stack.pop()
    
    def top(self): 
        if self.isempty():
            return None  # return None if stack is empty
        else:
            return self.stack[-1]


# # num=Stack()
# # num.push(3)
# # num.push(8)
# # num.push(11)
# # num.push(10)
# # num.pop()
# # print(num.top())
# # print(num.stack)
# # print(num.isempty())

# exp---string 
def infix_to_postfix(exp):
    obj = Stack()
    output = []
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '^': 3,'(':0}
    for i in exp:
        if i.isalnum():
            output.append(i)
        else:
            if i == '(':
                obj.push(i)
            elif obj.isempty():
                obj.push(i)
            elif i == ')':
                while obj.top() != '(':
                    a = obj.pop()
                    output.append(a)
                obj.pop()  # pop the '('
            elif precedence[i] > precedence[obj.top()]:
                obj.push(i)
            else:
                while not obj.isempty() and precedence[i] <= precedence[obj.top()]:
                    b = obj.pop()
                    output.append(b)
                obj.push(i)
    while not obj.isempty():
        c = obj.pop()
        output.append(c)
    return ''.join(output)

exp = 'A*B-(C+D)+E'
print(infix_to_postfix(exp))

# def postfixToInfix(exp):
#     stack=Stack()
#     output=[]
#     for i in exp:
#         if i.isalnum():
#             stack.push(i)
#         else:
#             op1=stack.pop()
#             op2=stack.pop()
#             string=op2+i+op1
#             stack.push(string)
#     output.append(stack.pop())
#     return output
# exp='ab+cde/*-f+'
# print(postfixToInfix(exp))




