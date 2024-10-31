class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Append a new node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def deleteAtLocation(self, position):
        """Delete the node at the given position."""
        if self.head is None:
            return  
        
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        count = 0
        
        while current is not None and count < position:
            prev = current
            current = current.next
            count += 1
        
        if current is None:
            return
        
        prev.next = current.next
    
    def printList(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)

print("Original Linked List:")
ll.printList()

ll.deleteAtLocation(0)
print("After deleting node at position 0:")
ll.printList()

ll.deleteAtLocation(3)
print("After deleting node at position 3:")
ll.printList()