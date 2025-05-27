from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None

def get_length(head: Node) -> int:
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def get_intersection_node(headA: Node, headB: Node) -> Optional[Node]:
    lenA = get_length(headA)
    lenB = get_length(headB)

    # Align heads
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Move together until match
    while headA and headB:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


# Shared part
common = Node(7)
common.next = Node(8)

# List A
headA = Node(1)
headA.next = Node(2)
headA.next.next = Node(3)
headA.next.next.next = common

# List B
headB = Node(4)
headB.next = Node(5)
headB.next.next = common

# Find intersection
result = get_intersection_node(headA, headB)
if result:
    print("Intersection at:", result.data)  # Output: Intersection at: 7
else:
    print("No intersection")
