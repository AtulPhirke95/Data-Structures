"""
Segregate even and odd nodes in a Linked List

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next =None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,key):
        temp = self.head
        if temp == None:
            new_node = Node(key)
            new_node.next = self.head
            self.head=new_node
        else:
            while temp.next!=None:
                temp=temp.next
            new_node = Node(key)
            temp.next = new_node
            new_node.next = None
    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def insertion_at_beginning(self,key):
        temp = self.head
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        
    def insertion_at_end(self,key):
        temp = self.head
        if temp==None:
            self.insertion_at_beginning(key)
        else:
            while(temp.next!=None):
                temp=temp.next
            new_node = Node(key)
            temp.next = new_node
            new_node.next = None
    
    def __add__(self,other):
        temp = self.head
        temp_=other.head

        while(temp.next!=None):
            if temp.data % 2 == 0:
                other.insertion_at_beginning(temp.data)
            elif temp.data % 2 == 1:
                other.insertion_at_end(temp.data)
            temp=temp.next
        
lobj = LinkedList()
lobj1 = LinkedList()

for i in range(1,11):
    lobj.push(i)
#lobj1.push(9999)

lobj+lobj1
lobj1.traversal()
