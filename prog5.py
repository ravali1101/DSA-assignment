class stack:
	def __init__(self):
		self._data = []

	def push(self,e):
		self._data.append(e)

	def pop(self):
		return self._data.pop()

	def is_empty (self):
		
		return len(self._data) == 0


def test_match_html (raw):
	S = stack()
	j = raw.find('<')

	while j != -1:
		l = raw.find(' ', j+1)
		k = raw.find('>', j+1)
		if k == -1:
			return False
		if l < k:
			tag = raw[j+1 : l]
		else:
			tag = raw[j+1 : k]
		if not tag.startswith('/'):
			S.push(tag)
		else:
			if S.is_empty():
				return False
			if tag[1:] != S.pop():
				return False

		j = raw.find('<',k+1)

	return S.is_empty()

if __name__ == '__main__' :
	print (test_match_html('<html> <body> <center> <h1> The DSA Assignment </h1> </center> </body> </html>'))
