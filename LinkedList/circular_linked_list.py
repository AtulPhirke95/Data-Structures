class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.last = None

	def push(self,key):
		temp = self.last
		if temp == None:
			new_node = Node(key)
			self.last = new_node
			self.last.next = self.last
		else:
			new_node = Node(key)
			new_node.next = self.last
			self.last = new_node

	def traversal(self):
		temp = self.last.next
		print(temp.data)
		temp=temp.next
		while temp.next != self.last:
			print(temp.data)
			temp =temp.next

if __name__=='__main__':
	lobj = LinkedList()
	lobj.push(1)
	lobj.push(2)
	lobj.push(3)
	lobj.traversal()