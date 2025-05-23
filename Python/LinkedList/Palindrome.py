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
        current: Node = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def is_palindrome(self) -> bool:
        if not self.head or not self.head.next:
            return True

        # Step 1: Find the middle (slow pointer)
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Compare both halves
        first_half = self.head
        second_half = prev
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
ll = LinkedList()
for val in [1, 2, 3, 2, 1]:
    ll.append(val)

ll.display()                        # 1 -> 2 -> 3 -> 2 -> 1 -> None
print(ll.is_palindrome())          # True
