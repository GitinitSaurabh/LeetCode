from typing import List, Optional

class Node:
    def __init__(self, value: int, prev_index: Optional[int]):
        self.value = value
        self.prev = prev_index

class ThreeStacks:
    def __init__(self, capacity: int = 100):
        self.array: List[Optional[Node]] = [None] * capacity
        self.free_index = 0
        self.stack_tops = [-1, -1, -1]  # Top index for each stack
        self.size = 0

    def push(self, stack_num: int, value: int) -> None:
        if self.size >= len(self.array):
            raise OverflowError("Stack overflow: no more space")

        node = Node(value, self.stack_tops[stack_num])
        self.array[self.free_index] = node
        self.stack_tops[stack_num] = self.free_index

        # Find next free index
        self.size += 1
        self._advance_free_index()

    def pop(self, stack_num: int) -> int:
        top_index = self.stack_tops[stack_num]
        if top_index == -1:
            raise IndexError(f"Stack {stack_num} is empty")

        node = self.array[top_index]
        self.stack_tops[stack_num] = node.prev
        self.array[top_index] = None
        self.size -= 1
        self.free_index = min(self.free_index, top_index)  # reclaim space
        return node.value

    def peek(self, stack_num: int) -> int:
        top_index = self.stack_tops[stack_num]
        if top_index == -1:
            raise IndexError(f"Stack {stack_num} is empty")
        return self.array[top_index].value

    def is_empty(self, stack_num: int) -> bool:
        return self.stack_tops[stack_num] == -1

    def _advance_free_index(self):
        while self.free_index < len(self.array) and self.array[self.free_index] is not None:
            self.free_index += 1


stacks = ThreeStacks(10)
stacks.push(0, 5)
stacks.push(1, 10)
stacks.push(2, 20)
stacks.push(0, 6)

print(stacks.pop(0))  # 6
print(stacks.peek(1)) # 10
print(stacks.pop(2))  # 20
