from typing import Optional
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional["Node"] = None
    
class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

        #Insert
    def append(self, data: int) -> None:
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        
        current: Node = self.head
        while current.next:
            current = current.next
        current.next = newNode
    
    def prepend(self, data: int) -> None:
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def delete(self, key: int) -> None:
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        
        prev: Optional[Node] = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current and prev:
            prev.next = current.next
        

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.display()  
ll.prepend(0)
ll.display()       # Output: 0 -> 1 -> 2 -> None
ll.delete(1)
ll.display()       # Output: 0 -> 2 -> None
