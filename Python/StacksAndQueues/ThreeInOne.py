 class ThreeStacks:
    def __init__(self, stack_size: int):
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)
        self.pointers = [0, 0, 0]  # Top index for each stack

    def push(self, stack_num: int, value: int) -> None:
        if self.pointers[stack_num] >= self.stack_size:
            raise OverflowError(f"Stack {stack_num} is full")
        
        index = stack_num * self.stack_size + self.pointers[stack_num]
        self.array[index] = value
        self.pointers[stack_num] += 1

    def pop(self, stack_num: int) -> int:
        if self.pointers[stack_num] == 0:
            raise IndexError(f"Stack {stack_num} is empty")
        
        self.pointers[stack_num] -= 1
        index = stack_num * self.stack_size + self.pointers[stack_num]
        value = self.array[index]
        self.array[index] = None
        return value

    def peek(self, stack_num: int) -> int:
        if self.pointers[stack_num] == 0:
            raise IndexError(f"Stack {stack_num} is empty")
        index = stack_num * self.stack_size + self.pointers[stack_num] - 1
        return self.array[index]

    def is_empty(self, stack_num: int) -> bool:
        return self.pointers[stack_num] == 0



stacks = ThreeStacks(5)  # 3 stacks, each of size 5
stacks.push(0, 10)
stacks.push(1, 20)
stacks.push(2, 30)

print(stacks.pop(0))  # Output: 10
print(stacks.peek(1)) # Output: 20
