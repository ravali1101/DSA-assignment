
class Stack:
	def __init__(self):		
	    self._data = []

	def push(self,e):
		self._data.append(e)

	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
		    return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0


	def reverse(self):
	    s = Stack()
	    t = Stack()
	    
	    length = len(self._data)

	    for e in range(length):
	    	s.push(self.pop())
	    
	    for e in range(length):
	    	t.push(s.pop())
	    	
	    for e in range(length):
	    	self._data.append(t.pop())

	    print(self._data)
	    


if __name__ == '__main__':
	s1 = Stack()
	s1.push(10)
	s1.push(20)
	s1.reverse()
