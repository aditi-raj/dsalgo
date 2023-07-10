#stack implementation

class Stack:
	def __init__(self):
		self.items = []

	def isempty(self):
		return self.items == []

	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	def top(self): 
		if self.isempty()==False:
			return self.items[-1]

#Conversion Problems using stack :

# def infix_to_postfix(exp):
#     obj=Stack()
#     output=[]
#     dict={'*':2,'/':2,'+':1,'-':1,'^':3}
#     for i in exp:
#         if i.isalnum():
#             output.append(i)
            
#         else:
#             if i=='(':
#                 obj.push(i)

#             if obj.isempty():
#                 obj.push(i)
#             elif i==')':
#                 while obj.top()!='(':
#                     a=obj.pop()
#                     output.append(a)
#                 obj.pop()
#             elif dict[i]>dict[obj.top()]:
#                 obj.push(i)
#             elif dict[i]<=dict[obj.top()]:
#                 b=obj.pop()
#                 output.append(b)
            
            

#     while obj.isempty()==False:
#         c=obj.pop()
#         output.append(c)
#     return output


# exp='a+b*c'
# print(infix_to_postfix(exp))

def prefixToInfix(exp):
	output=[]
	stack=Stack()
	exp=exp[::-1]
	for i in exp:
		if i.isalnum():
			stack.push(i)
		else:
			op1=stack.pop()
			op2=stack.pop()
			string=op1+i+op2
			stack.push(string)
	output.append(stack.pop())
	return output

exp='++A*BCD'
print(prefixToInfix(exp))

# def infixToPrefix(exp):
# 	new_exp=exp[::-1]
# 	out=infix_to_postfix(new_exp)
# 	return out[::-1]

# exp='a+b*c'
# print(infixToPrefix(exp))

