
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

if __name__ == '__main__':
	st = Stack()
	Lst = [10,20,30,40,50,60,70,80,90]
	length=len(Lst)
	print(length)
	
	for i in range(len(Lst)):
		st.push(Lst[i])
	
	Lst = []
	for i in range(length):
		Lst.append(st.pop())
	print(Lst)
