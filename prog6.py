class Stack:
	def __init__(self):		
	    self._data = []
	    self._size = 0

	def push(self,e):
		self._data.append(e)
		self._size += 1

	def pop(self):
		if(self.is_empty()):
			print("stack is empty")
		else:
			self._size -= 1
			return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

	def display(self):
		print(self._data)


def tests():
	R = Stack()
	st = Stack()
	T = Stack()

	R.push(1)
	R.push(2)
	R.push(3)
	R.display()
	
	S.push(4)
	S.push(5)
	S.display()

	T.push(6)
	T.push(7)
	T.push(8)
	T.push(9)
	T.display()

	while st.is_empty() == 0:
		(R.push(st.pop()))
		c += 1
	while T.is_empty() == 0:
		(R.push(T.pop()))
		c += 1
	R.display()

if __name__ == '__main__':
	tests()
