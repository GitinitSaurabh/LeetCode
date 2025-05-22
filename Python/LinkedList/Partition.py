from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def partition(self, x: int) -> None:
        before_head = before_tail = None
        after_head = after_tail = None

        current = self.head
        while current:
            node_next = current.next
            current.next = None
            if current.data < x:
                if not before_head:
                    before_head = before_tail = current
                else:
                    before_tail.next = current
                    before_tail = current
            else:
                if not after_head:
                    after_head = after_tail = current
                else:
                    after_tail.next = current
                    after_tail = current
            current = node_next
            
        if before_tail:
            before_tail.next = after_head
            self.head = before_head
        else:
            self.head = after_head
    
    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current: Node = self.head
        while current.next:
            current = current.next
        current.next = new_node


ll = LinkedList()
for val in [3, 5, 8, 5, 10, 2, 1]:
    ll.append(val)

ll.display()        # 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
ll.partition(5)
ll.display()        # 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10 -> None
