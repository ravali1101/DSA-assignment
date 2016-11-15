class Stack:
""" implementation of stack"""
""" create an empty stack"""
	def __init__(self):		
	    self._data = []
""" insert element into stack"""
	def push(self,x):
		self._data.append(x)
""" delete element from stack"""
	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
		    return self._data.pop()
""" check if stack is empty"""
	def is_empty(self):
		return len(self._data) == 0
""" reverse elements of stack"""
	def reverse_elements(self):
	    temp1 = Stack()
	    temp2 = Stack()
	    
	    length = len(self._data)

	    for x in range(length):
	    	temp1.push(self.pop())
	    
	    for x in range(length):
	    	temp2.push(temp1.pop())
	    	
	    for x in range(length):
	    	self._data.append(temp2.pop())

	    print(self._data)
	    


if __name__ == '__main__':
	s1 = Stack()
	s1.push(5)
	s1.push(10)
	s1.reverse_elements()
		
