sorted_list = []
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def preorder_traversal(root):
	if root ==None:
		return
	print(root.data)
	preorder_traversal(root.left)
	preorder_traversal(root.right)

def inorder_traversal(root):
	if root ==None:
		return
	inorder_traversal(root.left)
	print(root.data)
	global sorted_list
	sorted_list.append(root.data)
	inorder_traversal(root.right)

def postrder_traversal(root):
	if root ==None:
		return
	postrder_traversal(root.left)
	postrder_traversal(root.right)
	print(root.data)

def insert(root,key):
	if root == None:
		root = Node(key)
		root.left = None
		root.right = None
	elif key < root.data:
		root.left = insert(root.left, key)
	elif key > root.data:
		root.right = insert(root.right,key)
	else:
		print("Can not insert data as it is already present")
	return root

def height(root):
	if root == None:
		return 0
	lheight = height(root.left)
	rheight = height(root.right)
	if lheight > rheight:
		return 1 + lheight
	else:
		return 1 + rheight

def binary_search(low,up,key):
	while(low<=up):
		mid = (low+up)/2
		if key > sorted_list[mid]:
			low = mid+1
		elif key < sorted_list[mid]:
			up = mid-1
		else:
			return mid

if __name__ == '__main__':
	root = None
	lis = [19,35,10,12,46,6,40,3,90,8]

	for i in lis:
		root = insert(root,i)

	inorder_traversal(root)
	print(sorted_list)
	len_sorted_list = len(sorted_list)
	print(binary_search(0,len_sorted_list-1,90))
	print("Height of binary tree is {}".format(height(root)))