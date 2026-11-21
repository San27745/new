
class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):

        if self.front == None:
            self.front = self.rear = new_node
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next == None:
            self.rear = new_node

    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


pq = PriorityQueue()

pq.enqueue(node(100, 2))
pq.enqueue(node(200, 1))
pq.enqueue(node(300, 6))
pq.enqueue(node(400, 3))
pq.enqueue(node(500, 5))

pq.display()
