class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        if self.instack:
            self.in2out()
        return self.outstack.pop()

    def peek(self) -> int:
        self.in2out()
        return self.outstack[-1]

    def empty(self) -> bool:
        return not self.instack and not self.outstack

    def in2out(self) -> None:
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())