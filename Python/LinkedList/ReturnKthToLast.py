from typing import Optional

class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None) -> None:
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"
    

def kth_to_last(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    first: Optional[ListNode] = head
    second: Optional[ListNode] = head

    for _ in range(k):
        if first is None:
            return None
        first = first.next
    
    while first:
        first = first.next
        second = second.next
        
    return second

def create_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def main() -> None:
    values = [10, 20, 30, 40, 50, 60]
    k = 3
    head = create_linked_list(values)
    print("Original list:")
    print(head)

    result = kth_to_last(head, k)
    if result:
        print(f"{k}th to last node: {result.val}")
    else:
        print(f"List is shorter than {k} elements.")

if __name__ == "__main__":
    main()
