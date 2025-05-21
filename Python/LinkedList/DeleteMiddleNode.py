from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional["Node"] = None

    
class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
    
    def delete_middle(self) -> None:
        if not self.head or not self.head.next:
            self.head = None
            return
    
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next


            
        if prev and slow:
            prev.next = slow.next
                

    def append(self, data: int) -> None:
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
for num in [1, 2, 3, 4, 5]:
    ll.append(num)

ll.display()          # 1 -> 2 -> 3 -> 4 -> 5 -> None
ll.delete_middle()
ll.display()          # 1 -> 2 -> 4 -> 5 -> None
