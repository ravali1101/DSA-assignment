class Stack:
""" LIFO stack implementation usinng Python list as underlying storage """
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

if __name__ == '__main__':
	s = Stack()
	List = [1,2,3,4,5,6,7,8,9]
	length=len(List)
	print(length)
	for i in range(len(List)):
		s.push(List[i])
	List = []
	for i in range(length):
		List.append(s.pop())
	print(List)
		
