class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

list = LinkedList()

length = int(input("Enter how many element you want to insert in the list: "))

counter = 0

while counter < length:
    
    element = input(f"Enter the element number {counter + 1} : ")
    list.append(element)
    counter+=1
    
print("List :")
 
list.printList()
