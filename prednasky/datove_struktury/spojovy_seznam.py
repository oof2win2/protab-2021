class Node:
	def __init__(self, value, address):
		self.value = value
		self.address = address

class Stack:
	def __init__(self):
		self.head = Node(None, None)
		self.end = Node(None, None)
	
	def append(self, newValue):
		nextNode = self.head.address
		while nextNode is not None:
			nextNode = nextNode.address
		nextNode.address = Node(newValue, None)
		self.end = nextNode
		return nextNode

	def remove(self):
		nextNode = self.head
		while nextNode is not None:
			nextNode = nextNode.address
		if nextNode == self.head:
			return None
		output = nextNode.value
		nextNode = None
		return output
	
	def getAllValues(self):
		values = []
		nextNode = self.head
		while nextNode is not None:
			values.append(nextNode.value)
		return values

l = Stack()
l.append(3)
l.append(4)
print(l.getAllValues())