class Node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def traversal(self):
		temp = self.head
		while temp!=None:
			print(temp.data)
			temp = temp.next

	def push(self,key):
		temp = self.head
		if temp == None:
			new_node = Node(key)
			new_node.next = None
			new_node.prev = None
			self.head = new_node
		else:
			while temp.next!=None:
				temp = temp.next

			new_node = Node(key)
			new_node.next = None
			temp.next = new_node	
			new_node.prev = temp

	def insertion_at_beginning(self,key):
		temp = self.head
		if temp == None:
			self.push(key)
		else:
			new_node = Node(key)
			new_node.next = self.head
			new_node.prev = None
			new_node.next.prev = new_node
			self.head=new_node

	def insertion_in_between(self,key,new_key):
		temp = self.head
		if temp == None:
			self.push(new_key)
		else:
			while temp.data !=key:
				temp = temp.next
			new_node = Node(new_key)
			new_node.next = temp.next
			new_node.prev = temp
			temp.next = new_node
			new_node.next.prev = new_node
	
	def pop(self):
		temp = self.head
		if temp == None:
			print("Can not delete. List is empty.")
			return
		else:
			if temp.next ==None:
				self.head.next = None
				self.head.prev = None
			else:
				while(temp.next!=None):
					temp = temp.next
				temp.prev.next=None
				temp.prev = None
	def pop_at(self,key):
		temp = self.head
		flag = False
		while temp!=None:
			if temp.data ==key:
				flag=True
			temp = temp.next
		if flag == False:
			print("Serached key not found.")
			return
		else:	

			temp = self.head
			while temp.data != key:
				temp = temp.next
			temp.prev.next = temp.next
			temp.next.prev = temp.prev
			temp.next=None
			temp.prev = None

	def reversed(self):
		p1 = self.head
		p2 = p1.next
		p1.next = None
		p1.prev = p2
		while p2!=None:
			p2.prev = p2.next
			p2.next = p1
			p1 = p2
			p2 = p2.prev
			
		self.head = p1

if __name__== "__main__":
	lobj = LinkedList()
	for i in range(1,11):
		lobj.push(i)
		#pass
	#lobj.insertion_in_between(5,60)
	#lobj.pop()

	#lobj.pop_at(9)	
	lobj.reversed()
	lobj.traversal()