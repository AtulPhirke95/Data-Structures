class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def inorder_traversal(root):
	if root == None:
		return
	inorder_traversal(root.left)
	print(root.data)
	inorder_traversal(root.right)

def insert(root,key):
	if root is None:
		root = Node(key)
		root.left = None
		root.right = None
	elif key < root.data:
		root.left = insert(root.left,key)
	elif key > root.data:
		root.right = insert(root.right,key)
	return root

def delete_node_of_no_child(root,ptr,par):
	if par == None:
		root = None
	elif ptr == par.left:
		par.left = None
	elif ptr == par.right:
		par.right = None
	return root

def delete_node_of_one_child(root,ptr,par):
	if ptr.left != None:
		child = ptr.left
	elif ptr.right != None:
		child = ptr.right
	if par == None:
		root = child
	elif ptr == par.left:
		par.left = child
	elif ptr == par.right:
		par.right = child
	return root

def delete_node_of_two_child(root,ptr,par):
	parsucc = ptr
	succ = ptr.right
	while(succ.left!=None):
		parsucc = succ
		succ = succ.left
	ptr.data = succ.data
	if succ.left == None and succ.right == None:
		delete_node_of_no_child(root,succ,parsucc)
	else:
		delete_node_of_one_child(root,succ,parsucc)
	return root

def delete_decider(root,key):
	ptr = root
	par = None
	while(ptr != None):
		if key == ptr.data:
			break
		par = ptr

		if key < ptr.data:
			ptr = ptr.left
		elif key > ptr.data:
			ptr = ptr.right

	if ptr == None:
		print("Key not found")
		return
	elif ptr.left != None and ptr.right != None:
		root = delete_node_of_two_child(root,ptr,par)
	elif ptr.left !=None:
		root = delete_node_of_one_child(root,ptr,par)
	elif ptr.right != None:
		root = delete_node_of_one_child(root,ptr,par)
	elif ptr.left == None and ptr.right == None:
		root = delete_node_of_no_child(root,ptr,par)
	return root

if __name__ == '__main__':
	root = Node(67)
	root.left = Node(34)
	root.right = Node(80)
	root.left.left = Node(20)
	root.right.left = Node(78)

	inorder_traversal(root)
	print("_________________________________________")
	key = 67
	new_root = delete_decider(root,key)
	inorder_traversal(root)