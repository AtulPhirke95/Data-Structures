stack = []
queue = []
class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def stack_empty():
	global stack
	if len(stack) == 0:
		return 1
	else:
		return 0

def queue_empty():
	global queue
	if len(queue) == 0:
		return 1
	else:
		return 0

def preorder_traversal(root):
	if root == None:
		return
	global stack
	stack.append(root)
	while(stack_empty()!=1):
		ptr = stack.pop()
		print(ptr.data)
		if ptr.right != None:
			stack.append(ptr.right)

		if ptr.left != None:
			stack.append(ptr.left)

def inorder_traversal(root):
	if root == None:
		return
	global stack
	while 1:
		while(root.left != None):
			stack.append(root)
			root = root.left
		while(root.right == None):
			print(root.data)
			if stack_empty() == 1:
				return
			root = stack.pop()
		print(root.data)
		root = root.right

def postorder_traversal(root):
	q=root
	if root == None:
		return
	global stack
	while 1:
		while(root.left != None):
			stack.append(root)
			root = root.left
		while(root.right == None or root.right == q):
			print(root.data)
			q = root
			if stack_empty() == 1:
				return
			root = stack.pop()
		print(root.data)
		root = root.right

def level_order_traversal(root):
	if root == None:
		return
	global stack
	queue.append(root)
	while(queue_empty()!=1):
		ptr = queue.pop(0)
		print(ptr.data)
		if ptr.left != None:
			queue.append(ptr.left)

		if ptr.right != None:
			queue.append(ptr.right)

if __name__ == '__main__':
	root = Node(67)
	root.left = Node(34)
	root.right = Node(80)
	root.left.left = Node(20)
	root.right.left = Node(78)
	root.right.right = Node(100)
	#preorder_traversal(root)
	#inorder_traversal(root)
	#postorder_traversal(root)
	level_order_traversal(root)