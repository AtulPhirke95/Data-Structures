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

    def deleting_at_beginning(self):
        temp =self.head
        self.head = self.head.next

    def delete(self,key):
        temp=self.head
        if temp.data==key:
            self.head=self.head.next
        else:
            while temp.next.data!=key:
                temp=temp.next
            temp.next = temp.next.next    


    def length(self):
        temp=self.head
        count=0
        while temp.next!=None:
            count+=1
            temp=temp.next
        return count

    def add(self):
        temp = self.head
        l = self.length()
        i = 0
        while(i<=l):
            if temp.data % 2 != 0:
                print("odd",temp.data)
                #print(temp.data)
                self.insertion_at_end(temp.data)
                self.delete(temp.data)
            else:
                print("even",temp.data)
            temp=temp.next
            i+=1


    def reverse(self):
        temp = self.head
        prev = None
        next = None
        while temp!=None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
        
lobj = LinkedList()


for i in range(1,11):
    lobj.push(i)

#obj.traversal()
#lobj.delete(5)
lobj.add()
#print("__________________")
lobj.traversal()
#lobj.reverse()
#print("________________")
#lobj.traversal()
