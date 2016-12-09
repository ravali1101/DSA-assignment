class Stack:
	def __init__(self):		
	    self._data = []

	def push(self,e):
		self._data.append(e)

	def pop(self):
		if(self.is_empty()):
			print("stack  empty")
		else:
		    return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

	def reverse(self, r):
	    for e in range(len(self._data)):
	        r.push(self.pop())

	    print(r._data)	
	    

	    
if __name__ == '__main__':
	s = Stack()
	r= Stack()
	s.push(10)
	s.push(20)
	s.reverse(r)