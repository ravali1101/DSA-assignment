class Stack:
""" stack implementation usinng Python list as underlying storage """
""" Creat an empty stack """
	def __init__(self):		
	    self._data = []
""" Add element e to the top of the Stack """
	def push(self,x):
		self._data.append(x)
""" Remove and return the element from the top of the stack"""
	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
		    return self._data.pop()
""" Return True if the stack is empty """
	def is_empty(self):
		return len(self._data) == 0
"""copy the reversed stack"""
	def copy_reverse(self, T):
	    for x in range(len(temp1)):
	        T.push(self.pop())

	    print(T._data)	
	    

	    
if __name__ == '__main__':
	S = Stack()
	T = Stack()
	S.push(5)
	S.push(10)
	S.copy_reverse(T)
		
