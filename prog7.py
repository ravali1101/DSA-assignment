class stack:
	def __init__(self):
		self._data = []

	def push(self,e):
		self._data.append(e)

	def pop(self):
		return self._data.pop()

	def length(self):
		return len(self._data)

	def display(self):
		print(self._data)

class queue:
	def __init__(self):
		self.s1 = stack()
		self.s = stack()


	def enqueue(self,e):
		if self.s.length() == 0:
			self.s.push(ele)
		else:
			self.s1.push(self.s.pop())
			self.s1.push(e)
			for i in range(self.s1.length()):
				self.s.push(self.s1.pop())
		self.s.display()

	def dequeue(self):
		return self.s.pop()


if __name__ == '__main__':
	q = Queue()
	q.enqueue(10)
	q.enqueue(15)
	print(q.dequeue())

main()
