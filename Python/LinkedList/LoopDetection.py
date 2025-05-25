from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def has_cycle(self) -> bool:
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def create_cycle(self, pos: int) -> None:
        """Creates a cycle at position `pos` (0-indexed)."""
        if pos < 0:
            return

        tail = self.head
        cycle_node = None
        index = 0

        while tail and tail.next:
            if index == pos:
                cycle_node = tail
            tail = tail.next
            index += 1

        if tail and cycle_node:
            tail.next = cycle_node

ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)

ll.create_cycle(2)  # Create a cycle at node with value 3

print(ll.has_cycle())  # Output: True
