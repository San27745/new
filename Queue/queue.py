#linear queue using linkedlist
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        temp=self.front
        print("deleted node: ",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("queue is empty")
            self.rear=None
        temp=None
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next

q=Queue()
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))
q.dequeue()
q.dequeue()
q.dequeue()
q.print()