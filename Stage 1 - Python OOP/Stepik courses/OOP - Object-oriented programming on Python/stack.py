from typing import Any


class Stack:
    def __init__(self):
        self.values: list[Any] = []

    def push(self, item: Any):
        self.values.append(item)

    def pop(self) -> Any:
        if not self.is_empty():
            return self.values.pop()
        print("Empty Stack")

    def peek(self) -> Any:
        if not self.is_empty():
            return self.values[-1]
        print("Empty Stack")
        return None

    def is_empty(self) -> bool:
        return not self.values

    def size(self) -> int:
        return len(self.values)
