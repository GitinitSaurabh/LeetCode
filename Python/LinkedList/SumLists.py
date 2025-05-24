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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    @staticmethod
    def sum_lists(l1: Node, l2: Node) -> Node:
        carry = 0
        dummy_head = Node(0)
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            current.next = Node(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next


l1 = LinkedList()
l2 = LinkedList()

for num in [7, 1, 6]:  # 617
    l1.append(num)
for num in [5, 9, 2]:  # 295
    l2.append(num)

result = LinkedList()
result.head = LinkedList.sum_lists(l1.head, l2.head)

result.display()  # Output: 2 -> 1 -> 9 -> None
