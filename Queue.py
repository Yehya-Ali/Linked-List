class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return not self.head

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

q = Queue()
for _ in range(int(input("Count: "))):
    q.enqueue(input("Element: "))
print("Queue:"); q.print()
print("Dequeued:");
while not q.is_empty(): print(q.dequeue(), end=' ')
print("\nQueue after dequeue:");q.print()
