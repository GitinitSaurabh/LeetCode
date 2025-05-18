from typing import Optional

class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"
    

def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:

    seen: set[int] = set()
    current: Optional[ListNode] = head
    prev: Optional[ListNode] = None

    while current:
        if current.val in seen:
            prev.next = current.next
        else:
            seen.add(current.val)
            prev = current
        current = current.next
    
    return head

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 🔹 Driver code
if __name__ == "__main__":
    values = [1, 2, 3, 2, 4, 1, 5]
    head = create_linked_list(values)
    print("Original linked list:")
    print(head)

    updated_head = remove_duplicates(head)
    print("After removing duplicates:")
    print(updated_head)